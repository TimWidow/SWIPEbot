from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.callbacks.user_callback import POST_FILTER_CB, get_detail_callback_with_page


ITEM_CB = POST_FILTER_CB


state_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(('После ремонта'), callback_data=ITEM_CB.new(action='add_state',
                                                                               value='BLANK')),
    InlineKeyboardButton(('Черновая'), callback_data=ITEM_CB.new(action='add_state',
                                                                          value='ROUGH')),
    InlineKeyboardButton(('Евроремонт'), callback_data=ITEM_CB.new(action='add_state',
                                                                            value='EURO')),
    InlineKeyboardButton(('Требует ремонта'), callback_data=ITEM_CB.new(action='add_state',
                                                                                 value='NEED'))
)


foundation_doc_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(('Собственность'), callback_data=ITEM_CB.new(action='add_doc',
                                                                               value='OWNER')),
    InlineKeyboardButton(('Аренда'), callback_data=ITEM_CB.new(action='add_doc',
                                                                        value='RENT'))
)


plan_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(('Свободная планировка'), callback_data=ITEM_CB.new(action='add_plan',
                                                                                      value='FREE')),
    InlineKeyboardButton(('Студия'), callback_data=ITEM_CB.new(action='add_plan',
                                                                        value='STUDIO')),
    InlineKeyboardButton(('Смежные комнаты'), callback_data=ITEM_CB.new(action='add_plan',
                                                                                 value='ADJACENT'))
).add(
    InlineKeyboardButton(('Изолированные комнаты'), callback_data=ITEM_CB.new(action='add_plan',
                                                                                       value='ISOLATED')),
    InlineKeyboardButton(('Малосемейка'), callback_data=ITEM_CB.new(action='add_plan',
                                                                             value='SMALL')),
    InlineKeyboardButton(('Гостинка'), callback_data=ITEM_CB.new(action='add_plan',
                                                                          value='ROOM'))
)


balcony_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(('Есть'), callback_data=ITEM_CB.new(action='add_balcony',
                                                                      value='YES')),
    InlineKeyboardButton(('Нет'), callback_data=ITEM_CB.new(action='add_balcony',
                                                                     value='NO'))
)


flat_type_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton(('Апартаменты'), callback_data=ITEM_CB.new(action='add_type',
                                                                             value='FLAT')),
    InlineKeyboardButton(('Офис'), callback_data=ITEM_CB.new(action='add_type',
                                                                      value='OFFICE')),
    InlineKeyboardButton(('Студия'), callback_data=ITEM_CB.new(action='add_type',
                                                                        value='STUDIO'))
)


async def get_floors_keyboard(items: list) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for index, item in enumerate(items, start=1):
        markup.insert(
            InlineKeyboardButton(str(index), callback_data=ITEM_CB.new(action='add_floor',
                                                                       value=item['id']))
        )
    return markup
