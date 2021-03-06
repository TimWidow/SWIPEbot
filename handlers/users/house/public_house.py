import os
from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher import FSMContext
from loader import dp, Conn, log
from keyboards.default.dispatcher import dispatcher
from keyboards.inline.user_keyboards import (get_keyboard_for_list, get_keyboard_for_house, get_keyboard_for_my_house,
                                             get_keyboard_for_flat, get_keyboard_for_flat_list, get_keyboard_for_booked_flat,
                                             get_keyboard_for_flat_detail_house, get_keyboard_for_my_flat,
                                             get_keyboard_for_document_detail)
from keyboards.inline import create_house
from keyboards.callbacks.user_callback import LIST_CB, DETAIL_WITH_PAGE_CB, DETAIL_CB, LIST_CB_WITH_PK
from deserializers.house import HouseDeserializer, FlatDeserializer
from handlers.users.utils import handle_list, send_with_image
from utils.session.url_dispatcher import REL_URLS
from utils.db_api.models import User, File
house_des = HouseDeserializer()
flat_des = FlatDeserializer()


keyboard_house_detail = {
    'house_detail': get_keyboard_for_house,
    'my_house_detail': get_keyboard_for_my_house,
    'from_flat_house_detail': get_keyboard_for_flat_detail_house
}
keyboard_flat_detail = {
    'flat_detail': get_keyboard_for_flat,
    'my_flat_detail': get_keyboard_for_my_flat,
    'booked_flat': get_keyboard_for_booked_flat
}


async def get_house(call: types.CallbackQuery, callback_data: dict,
                    keyboard_key: str):
    keyboard_cor = keyboard_house_detail[keyboard_key]
    log.debug(callback_data)
    pk = callback_data.get('pk')
    url = f'{REL_URLS["houses_public"]}{pk}/'
    resp = await Conn.get(url, user_id=call.from_user.id)
    inst = await house_des.for_detail(resp)
    if keyboard_key == 'house_detail':
        keyboard = await keyboard_cor(page=callback_data.get('page'),
                                      key=callback_data.get('key'),
                                      action='house_list_new' if resp.get('image') else 'house_list',
                                      pk=pk)
    elif keyboard_key == 'from_flat_house_detail':
        keyboard = await keyboard_cor(page=callback_data.get('page'),
                                      key=callback_data.get('key'),
                                      action='my_apartments_list')
    else:
        keyboard = await keyboard_cor(page=callback_data.get('page'),
                                      key=callback_data.get('key'),
                                      action='my_house_list_new' if resp.get('image') else 'my_house_list',
                                      pk=pk)
    if resp.get('image'):
        await send_with_image(call, resp, pk, inst.data, keyboard,
                              'image')
    else:
        await call.message.answer(inst.data, reply_markup=keyboard)
    await call.answer()


async def get_flat(call: types.CallbackQuery, callback_data: dict,
                   keyboard_key: str):
    keyboard_cor = keyboard_flat_detail[keyboard_key]
    log.debug(callback_data)
    pk = callback_data.get('pk')
    url = f'{REL_URLS["apartments_public"]}{pk}/'
    resp = await Conn.get(url, user_id=call.from_user.id)
    inst = await flat_des.for_detail(resp)
    if keyboard_key == 'booked_flat':
        action = 'my_apartments_list'
    else:
        action = 'apartments_list'
    keyboard = await keyboard_cor(key=callback_data.get('key'),
                                  page=callback_data.get('page'),
                                  action=action,
                                  pk=pk,
                                  house_pk=resp.get('house_pk'))
    await send_with_image(call, resp, pk, inst.data, keyboard, 'schema')
    await call.answer()


@dp.message_handler(Text(equals=['???????????? ??????????', 'List houses']))
async def get_house_keyboard(message: types.Message, state: FSMContext):
    keyboard, path = await dispatcher('LEVEL_2_HOUSES', message.from_user.id)
    log.debug(path)
    await message.answer('???????? ??????????', reply_markup=keyboard)
    await state.update_data(path=path)


@dp.message_handler(Text(equals=['?????? ????????', 'All houses']))
async def house_list(message: types.Message, state: FSMContext):
    params = await state.get_data()
    await message.answer('???????????? ???????? ??????????')
    await handle_list(message, key='houses_public', page='1', deserializer=house_des,
                      keyboard=get_keyboard_for_list, detail_action='house_detail',
                      list_action='house_list', params=params)


@dp.callback_query_handler(LIST_CB.filter(action='house_list'))
async def house_list(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    page = callback_data.get('page')
    key = callback_data.get('key')
    params = await state.get_data()
    await handle_list(call, key=key, page=page, deserializer=house_des,
                      keyboard=get_keyboard_for_list, detail_action='house_detail',
                      list_action='house_list', params=params)


@dp.callback_query_handler(LIST_CB.filter(action='house_list_new'))
async def house_list_new(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    page = callback_data.get('page')
    key = callback_data.get('key')
    params = await state.get_data()
    await handle_list(call, key=key, page=page, params=params, keyboard=get_keyboard_for_list,
                      detail_action='house_detail', list_action='house_list',
                      deserializer=house_des, new_callback_answer=True)


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='house_detail'))
async def house_detail(call: types.CallbackQuery, callback_data: dict):
    await get_house(call, callback_data, 'house_detail')


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='from_flat_house_detail'))
async def house_detail(call: types.CallbackQuery, callback_data: dict):
    await get_house(call, callback_data, 'from_flat_house_detail')


@dp.message_handler(Text(equals=['?????? ????????', 'My houses']))
async def my_houses(message: types.Message, state: FSMContext):
    keyboard, path = await dispatcher('LEVEL_3_MY_HOUSES', message.from_user.id)
    params = await state.get_data()
    await message.answer('?????? ????????', reply_markup=keyboard)
    await handle_list(message, key='houses', page='1', params=params, keyboard=get_keyboard_for_list,
                      detail_action='my_house_detail', list_action='my_house_list',
                      deserializer=house_des)
    await state.update_data(path=path)


@dp.callback_query_handler(LIST_CB.filter(action='my_house_list'))
async def my_house_list(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    page = callback_data.get('page')
    key = callback_data.get('key')
    params = await state.get_data()
    await handle_list(call, key=key, page=page, deserializer=house_des,
                      detail_action='my_house_detail', list_action='my_house_list',
                      keyboard=get_keyboard_for_list, params=params)


@dp.callback_query_handler(LIST_CB.filter(action='my_house_list_new'))
async def my_house_list(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    page = callback_data.get('page')
    key = callback_data.get('key')
    params = await state.get_data()
    await handle_list(call, key=key, page=page, deserializer=house_des,
                      detail_action='my_house_detail', list_action='my_house_list',
                      keyboard=get_keyboard_for_list, params=params,
                      new_callback_answer=True)


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='my_house_detail'))
async def my_house_detail(call: types.CallbackQuery, callback_data: dict):
    await get_house(call, callback_data, 'my_house_detail')


@dp.callback_query_handler(DETAIL_CB.filter(action='delete_house'))
async def delete_house(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    pk = callback_data.get('pk')
    params = await state.get_data()
    url = f'{REL_URLS["houses"]}{pk}/'
    resp, status = await Conn.delete(url, user_id=call.from_user.id)
    if status == 204:
        await handle_list(call, key='houses', page='1', deserializer=house_des,
                          detail_action='my_house_detail', list_action='my_house_list',
                          keyboard=get_keyboard_for_list, params=params,
                          new_callback_answer=True)
        await call.answer('?????? ?????? ????????????')
    else:
        await call.answer('?????????????????? ????????????')


@dp.callback_query_handler(LIST_CB_WITH_PK.filter(action='apartments_list'))
async def house_apartments(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    key = callback_data.get('key')
    page = callback_data.get('page')
    params = callback_data.get('params')
    url = f'{REL_URLS["apartments_public"]}?house__pk={pk}&page={page}'
    await handle_list(call, key=key, page=page, params=params,
                      keyboard=get_keyboard_for_flat_list, detail_action='flat_detail',
                      list_action='apartments_list_edit', deserializer=flat_des,
                      new_callback_answer=True, custom_url=url, pk=pk)


@dp.callback_query_handler(LIST_CB_WITH_PK.filter(action='apartments_list_edit'))
async def house_apartments(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    key = callback_data.get('key')
    page = callback_data.get('page')
    params = callback_data.get('params')
    url = f'{REL_URLS["apartments_public"]}?house__pk={pk}&page={page}'
    await handle_list(call, key=key, page=page, params=params,
                      keyboard=get_keyboard_for_flat_list, detail_action='flat_detail',
                      list_action='apartments_list_edit', deserializer=flat_des,
                      custom_url=url, pk=pk)


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='flat_detail'))
async def flat_detail(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    url = f'{REL_URLS["apartments"]}{pk}/'
    resp = await Conn.get(url, user_id=call.from_user.id)
    user = await User.get(user_id=call.from_user.id)
    if resp.get('sales_department_pk') == user.swipe_id:
        key = 'my_flat_detail'
    else:
        key = 'flat_detail'
    await get_flat(call, callback_data, key)


@dp.callback_query_handler(DETAIL_CB.filter(action='booking_flat'))
async def booking_flat(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    url = REL_URLS['booking_flat'].format(flat_pk=pk)
    data = {'booking': '1'}
    resp = await Conn.patch(url, data=data, user_id=call.from_user.id)
    if resp.get('Error'):
        await call.message.answer('?????????????????? ????????????')
        await call.answer(resp.get('Error'), show_alert=True)
    else:
        await call.answer('???????????????? ??????????????????????????. ???????????? ???? ???????????????????? ?? ???????????????? ?????????????????? ???????????????????????????? ????????',
                          show_alert=True)


@dp.message_handler(Text(equals=['?????? ????????????????', 'My apartments']))
async def my_apartments(message: types.Message):
    await message.answer('???????????? ?????????????????????????????? ??????????????')
    user = await User.get(user_id=message.from_user.id)
    url = f'{REL_URLS["apartments_public"]}?client_pk={user.swipe_id}&page=1'
    await handle_list(message, key='apartments', page='1',
                      keyboard=get_keyboard_for_flat_list,
                      detail_action='my_flat_detail', list_action='my_apartments_list',
                      deserializer=flat_des, pk=0, custom_url=url)


@dp.callback_query_handler(LIST_CB_WITH_PK.filter(action='my_apartments_list'))
async def my_apartments_callback(call: types.CallbackQuery, callback_data: dict):
    key = callback_data.get('key')
    page = callback_data.get('page')
    user = await User.get(user_id=call.from_user.id)
    url = f'{REL_URLS["apartments_public"]}?client_pk={user.swipe_id}&page={page}'
    await handle_list(call, key=key, page=page,
                      keyboard=get_keyboard_for_flat_list,
                      detail_action='my_flat_detail', list_action='my_apartments_list',
                      deserializer=flat_des, pk=0, custom_url=url, new_callback_answer=True)


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='my_flat_detail'))
async def my_flat_detail(call: types.CallbackQuery, callback_data: dict):
    await get_flat(call, callback_data, keyboard_key='booked_flat')


@dp.callback_query_handler(DETAIL_CB.filter(action='unbooking_flat'))
async def unbooking_flat(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    url = REL_URLS['booking_flat'].format(flat_pk=pk)
    data = {'booking': '0'}
    resp = await Conn.patch(url, data=data, user_id=call.from_user.id)
    if resp.get('Error'):
        await call.message.answer('?????????????????? ????????????')
        await call.answer(resp.get('Error'), show_alert=True)
    else:
        await call.answer('?????????? ??????????', show_alert=True)
        user = await User.get(user_id=call.from_user.id)
        url = f'{REL_URLS["apartments_public"]}?client_pk={user.swipe_id}&page=1'
        await handle_list(call, key='apartments', page='1',
                          keyboard=get_keyboard_for_flat_list ,
                          detail_action='my_flat_detail', list_action='my_apartments_list',
                          deserializer=flat_des, pk=0, custom_url=url, new_callback_answer=True)


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='add_block'))
async def add_block(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    resp, status = await Conn.post(REL_URLS['blocks'], data={'house': pk}, user_id=call.from_user.id)
    if status == 201:
        await call.answer('???????????? ????????????????', show_alert=True)
        await get_house(call, callback_data, 'my_house_detail')
    else:
        await call.answer('?????????????????? ????????????')
        for key, value in resp.items():
            log.info(f'{key}: {value}\n')


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='add_section'))
async def add_section(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    page = callback_data.get('page')
    key = callback_data.get('key')
    resp = await Conn.get(REL_URLS['blocks'], params={'house': pk}, user_id=call.from_user.id)
    blocks = resp.get('results')
    if blocks:
        keyboard = await create_house.get_block_keyboard(items=resp.get('results'), action='add_section_block',
                                                            page=page, key=key)
        text = ''
        for index, item in enumerate(blocks, start=1):
            text += f'{index}. {item["full_name"]}\n'
        await call.message.answer(text, reply_markup=keyboard)
        await call.answer()
    else:
        await call.answer(('?????? ????????????????. ???????????? ???????????????? ????'), show_alert=True)


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='add_section_block'))
async def save_section(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    resp, status = await Conn.post(REL_URLS['sections'], data={'block': pk}, user_id=call.from_user.id)
    if status == 201:
        callback_data['pk'] = resp['house']
        await call.answer(('???????????? ??????????????????'), show_alert=True)
        await get_house(call, callback_data, 'my_house_detail')
    else:
        await call.answer(('?????????????????? ????????????'))
        for key, value in resp.items():
            log.info(f'{key}: {value}\n')


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='add_floor'))
async def add_floor(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    page = callback_data.get('page')
    key = callback_data.get('key')
    resp = await Conn.get(REL_URLS['sections'], params={'house': pk}, user_id=call.from_user.id)
    sections = resp.get('results')
    if sections:
        keyboard = await create_house.get_block_keyboard(items=resp.get('results'), action='add_floor_section',
                                                            page=page, key=key)
        text = ''
        for index, item in enumerate(sections, start=1):
            text += f'{index}. {item["full_name"]}\n'
        await call.message.answer(text, reply_markup=keyboard)
        await call.answer()
    else:
        await call.answer(('?????? ????????????. ???????????????? ???? ????????????'), show_alert=True)


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='add_floor_section'))
async def save_floor(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    resp, status = await Conn.post(REL_URLS['floors'], data={'section': pk}, user_id=call.from_user.id)
    if status == 201:
        callback_data['pk'] = resp['house']
        await call.answer(('???????? ????????????????'), show_alert=True)
        await get_house(call, callback_data, 'my_house_detail')
    else:
        await call.answer(('?????????????????? ????????????'))
        for key, value in resp.items():
            log.info(f'{key}: {value}\n')


@dp.callback_query_handler(DETAIL_CB.filter(action='delete_flat'))
async def delete_flat(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    url = f'{REL_URLS["apartments"]}{pk}/'
    resp = await Conn.get(url, user_id=call.from_user.id)
    resp_delete, status = await Conn.delete(url, user_id=call.from_user.id)
    if status == 204:
        await call.answer()
        data = {'pk': resp.get('house_pk'),
                'page': '1',
                'key': 'houses'}
        await get_house(call, data, 'my_house_detail')
    else:
        await call.answer(('?????????????????? ????????????. ???????????????????? ?????? ??????'))


@dp.callback_query_handler(LIST_CB_WITH_PK.filter(action='house_structure_list'))
async def house_structure_list(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    key = callback_data.get('key')
    resp = await Conn.get(REL_URLS[key], params={'house': pk}, user_id=call.from_user.id)
    objects = resp.get('results')
    if objects:
        keyboard = await create_house.get_block_keyboard(items=objects,
                                                            page=callback_data.get('page'),
                                                            key=key,
                                                            action='delete_house_structure')
        text = ''
        for index, item in enumerate(objects, start=1):
            text += f'{index}. {item["full_name"]}\n'
            text += f'???????? ?????????????????? ??????????????\n' if item.get('has_related') is True else '??????????\n'
        await call.message.answer(text, reply_markup=keyboard)
        await call.answer()
    else:
        await call.answer(('???????????? ??????'), show_alert=True)


@dp.callback_query_handler(DETAIL_WITH_PAGE_CB.filter(action='delete_house_structure'))
async def delete_house_structure(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    key = callback_data.get('key')
    url = f'{REL_URLS[key]}{pk}/'
    resp_detail = await Conn.get(url, user_id=call.from_user.id)
    resp, status = await Conn.delete(url, user_id=call.from_user.id)
    if status == 204:
        await call.answer(('???????????? ????????????'))
        if resp_detail.get('house'):
            callback_data['pk'] = resp_detail.get('house')
            callback_data['key'] = 'houses'
            await get_house(call, callback_data, 'my_house_detail')
        await call.message.delete()
    else:
        await call.answer(('?????????????????? ????????????: ' + status))


@dp.callback_query_handler(LIST_CB_WITH_PK.filter(action='news_list'))
async def news_list(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    resp = await Conn.get(REL_URLS['news'], params={'house': pk}, user_id=call.from_user.id)
    objects = resp.get('results')
    if objects:
        keyboard = await create_house.get_block_keyboard('delete_house_structure', objects,
                                                            'news', '1')
        text = ''
        for index, item in enumerate(objects, start=1):
            text += f'{index}. {item["title"]}\n'
        await call.message.answer(text, reply_markup=keyboard)
        await call.answer()
    else:
        await call.answer(('???????????????? ??????'))


@dp.callback_query_handler(LIST_CB_WITH_PK.filter(action='doc_list'))
async def docs_list(call: types.CallbackQuery, callback_data: dict):
    pk = callback_data.get('pk')
    resp = await Conn.get(REL_URLS['documents'], params={'house': pk}, user_id=call.from_user.id)
    documents = resp.get('results')
    if documents:
        for item in documents:
            resp_file = await Conn.get(item.get('file'), user_id=call.from_user.id)
            filename = os.path.split(item.get('file'))[-1]
            file_data = await File.get_or_none(filename=filename, parent_id=pk)

            if resp_file.get('file_type') in ('image/png', 'image/jpeg', 'image/jpg'):
                method = call.bot.send_photo
                file_attr = 'photo'
            else:
                method = call.bot.send_document
                file_attr = 'document'
            if file_data:
                await method(call.from_user.id, file_data.file_id,
                             reply_markup=await get_keyboard_for_document_detail(item['id']))
            else:
                msg = await method(call.from_user.id, resp_file.get('file'),
                                   reply_markup=await get_keyboard_for_document_detail(item['id']))
                if file_attr == 'photo':
                    file_id = msg.photo[-1].file_id
                else:
                    file_id = getattr(msg, file_attr).file_id
                await File.create(filename=filename,
                                  file_id=file_id,
                                  parent_id=pk)
        await call.answer()
    else:
        await call.answer(('???????????????????? ??????'))
