from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.callbacks import user_callback
from typing import Iterable
import emoji

lang_markup = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Русский', callback_data=user_callback.LANG_CB.new(action='lang',
                                                                                 lang='ru')),
    InlineKeyboardButton(text='English', callback_data=user_callback.LANG_CB.new(action='lang',
                                                                                 lang='en'))
)


async def get_detail_keyboard(action: str, title: str, pk: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(title, callback_data=user_callback.get_detail_callback(action, pk))
    )
    return markup


async def get_keyboard_for_list(items: Iterable, pages: dict, key: str,
                                detail_action: str, list_action: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=4)
    for index, item in enumerate(items, start=1):
        markup.insert(
            InlineKeyboardButton(text=f'{index}',
                                 callback_data=user_callback.get_detail_callback_with_page(action=detail_action,
                                                                                           pk=item.pk,
                                                                                           page=pages.get('current'),
                                                                                           key=key))
        )
    markup.add(
        InlineKeyboardButton(text='Назад', callback_data=user_callback.get_list_callback(action=list_action,
                                                                                                    page=pages.get('prev'),
                                                                                                    key=key)),
        InlineKeyboardButton(text='Новое',
                             callback_data=user_callback.get_list_callback(action=list_action,
                                                                           page=pages.get('first'),
                                                                           key=key)),
        InlineKeyboardButton(text='Вперед', callback_data=user_callback.get_list_callback(action=list_action,
                                                                                                     page=pages.get('next'),
                                                                                                     key=key))
    )

    return markup


async def get_keyboard_for_post_detail(page: str, pk: int, flat_pk: int, key: str,
                                       user_id: int = None, favorites: list = None) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(emoji.emojize(':thumbs_up:'),
                             callback_data=user_callback.LIKE_DISLIKE_CB.new(action='like_post',
                                                                             pk=pk,
                                                                             type='like',
                                                                             page=page,
                                                                             key=key)),
        InlineKeyboardButton(emoji.emojize(':thumbs_down:'),
                             callback_data=user_callback.LIKE_DISLIKE_CB.new(action='like_post',
                                                                             pk=pk,
                                                                             type='dislike',
                                                                             page=page,
                                                                             key=key))
    )
    if key == 'posts_public':
        markup.row(
            InlineKeyboardButton('Назад', callback_data=user_callback.get_list_callback(action='post_list_new',
                                                                                                   page=page,
                                                                                                   key=key)),
            InlineKeyboardButton('Пожаловаться',
                                 callback_data=user_callback.COMPLAINT_CB.new(action='complaint', pk=pk,
                                                                              type='_'))
        )
        if user_id in favorites:
            markup.insert(InlineKeyboardButton('Убрать из избранного',
                                               callback_data=user_callback.get_detail_callback_with_page(
                                                   action='delete_from_favorites',
                                                   pk=pk,
                                                   key=key,
                                                   page=page)))
        else:
            markup.insert(InlineKeyboardButton('В избранное',
                                               callback_data=user_callback.DETAIL_CB.new(action='save_to_favorites',
                                                                                         pk=pk)))
    elif key == 'favorites':
        markup.row(
            InlineKeyboardButton('Назад', callback_data=user_callback.get_list_callback(action='post_list_new',
                                                                                                   page=page,
                                                                                                   key=key)),
            InlineKeyboardButton('Пожаловаться', callback_data=user_callback.COMPLAINT_CB.new(action='complaint',
                                                                                                         pk=pk,
                                                                                                         type='_'))
        ).row(
            InlineKeyboardButton('Убрать из избранного',
                                 callback_data=user_callback.get_detail_callback_with_page(
                                     action='delete_from_favorites',
                                     pk=pk,
                                     key=key,
                                     page=page))
        )
    return markup


async def get_post_complaint_types(post_pk: int) -> InlineKeyboardMarkup:
    inline_markup = InlineKeyboardMarkup().row(
        InlineKeyboardButton('Неккоректная цена', callback_data=user_callback.COMPLAINT_CB.new(action='complaint',
                                                                                                          pk=post_pk,
                                                                                                          type='PRICE'))
    ).row(
        InlineKeyboardButton('Неккоректное фото', callback_data=user_callback.COMPLAINT_CB.new(action='complaint',
                                                                                                          pk=post_pk,
                                                                                                          type='PHOTO'))
    ).row(
        InlineKeyboardButton('Неккоректное описание',
                             callback_data=user_callback.COMPLAINT_CB.new(action='complaint',
                                                                          pk=post_pk,
                                                                          type='DESC'))
    )
    return inline_markup


async def get_keyboard_for_filter(items: Iterable) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=4)
    for index, item in enumerate(items, start=1):
        markup.insert(
            InlineKeyboardButton(text=f'{index}',
                                 callback_data=user_callback.get_detail_callback(action='filter_detail',
                                                                                 pk=item.pk))
        )

    return markup


async def get_keyboard_for_filter_detail(pk: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton('Назад', callback_data=user_callback.get_list_callback(action='filter_list',
                                                                                               page='1',
                                                                                               key='filter_list_new')),
        InlineKeyboardButton('Применить', callback_data=user_callback.get_detail_callback(action='set_filter',
                                                                                                     pk=pk))
    ).add(
        InlineKeyboardButton('Удалить', callback_data=user_callback.get_detail_callback(action='delete_filter',
                                                                                                   pk=pk))
    )
    return markup


async def get_keyboard_for_my_post_detail(page: str, pk: int, flat_pk: int, key: str, ) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='О квартире',
                             callback_data=user_callback.get_detail_callback(action='flat_detail',
                                                                             pk=flat_pk))
    ).add(
        InlineKeyboardButton(text='Заказать продвижение',
                             callback_data=user_callback.get_detail_callback(action='add_promotion',
                                                                             pk=pk)),
        InlineKeyboardButton(text='Убрать продвижение',
                             callback_data=user_callback.get_detail_callback(action='delete_promotion',
                                                                             pk=pk))
    )
    markup.row(
        InlineKeyboardButton('Назад', callback_data=user_callback.get_list_callback(action='my_post_list_new',
                                                                                               page=page,
                                                                                               key=key)),
        InlineKeyboardButton('Редактировать', callback_data=user_callback.get_detail_callback(action='edit_post',
                                                                                                         pk=pk)),
        InlineKeyboardButton('Удалить',
                             callback_data=user_callback.get_detail_callback_with_page(action='delete_post',
                                                                                       page=page,
                                                                                       key=key,
                                                                                       pk=pk))
    )
    return markup


async def get_keyboard_for_house(key: str, page: str, action: str, pk: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Квартиры', callback_data=user_callback.LIST_CB_WITH_PK.new(action='apartments_list',
                                                                                                         page='1',
                                                                                                         key='apartments',
                                                                                                         pk=pk)),
        InlineKeyboardButton('Документы', callback_data=user_callback.LIST_CB_WITH_PK.new(action='doc_list',
                                                                                                     page='1',
                                                                                                     key='news',
                                                                                                     pk=pk)),
    ).add(
        InlineKeyboardButton(text='Назад', callback_data=user_callback.get_list_callback(action=action,
                                                                                                    page=page,
                                                                                                    key=key))
    )
    return markup


async def get_keyboard_for_my_house(key: str, page: str, action: str, pk: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Редактировать',
                             callback_data=user_callback.get_detail_callback(action='edit_house',
                                                                             pk=pk)),
        InlineKeyboardButton(text='Удалить', callback_data=user_callback.get_detail_callback(action='delete_house',
                                                                                                        pk=pk))
    ).add(
        InlineKeyboardButton('Добавить корпус',
                             callback_data=user_callback.get_detail_callback_with_page(action='add_building',
                                                                                       pk=pk,
                                                                                       key=key,
                                                                                       page=page)),
        InlineKeyboardButton('Добавить секцию',
                             callback_data=user_callback.get_detail_callback_with_page(action='add_section',
                                                                                       pk=pk,
                                                                                       key=key,
                                                                                       page=page)),
        InlineKeyboardButton('Добавить этаж',
                             callback_data=user_callback.get_detail_callback_with_page(action='add_floor',
                                                                                       pk=pk,
                                                                                       key=key,
                                                                                       page=page))
    ).add(
        InlineKeyboardButton('Корпуса',
                             callback_data=user_callback.LIST_CB_WITH_PK.new(action='house_structure_list',
                                                                             page='1',
                                                                             key='buildings',
                                                                             pk=pk)),
        InlineKeyboardButton('Секции', callback_data=user_callback.LIST_CB_WITH_PK.new(action='house_structure_list',
                                                                                                  page='1',
                                                                                                  key='sections',
                                                                                                  pk=pk)),
        InlineKeyboardButton('Этажи', callback_data=user_callback.LIST_CB_WITH_PK.new(action='house_structure_list',
                                                                                                 page='1',
                                                                                                 key='floors',
                                                                                                 pk=pk))
    ).add(
        InlineKeyboardButton(text='Квартиры', callback_data=user_callback.LIST_CB_WITH_PK.new(action='apartments_list',
                                                                                                         page='1',
                                                                                                         key='apartments',
                                                                                                         pk=pk)),
        InlineKeyboardButton('Добавить квартиру', callback_data=user_callback.get_detail_callback(action='add_flat',
                                                                                                             pk=pk))
    ).add(
        InlineKeyboardButton('Новости', callback_data=user_callback.LIST_CB_WITH_PK.new(action='news_list',
                                                                                                   page='1',
                                                                                                   key='news',
                                                                                                   pk=pk)),
        InlineKeyboardButton('Добавить новость', callback_data=user_callback.get_detail_callback(action='add_news',
                                                                                                            pk=pk))
    ).add(
        InlineKeyboardButton('Документы', callback_data=user_callback.LIST_CB_WITH_PK.new(action='doc_list',
                                                                                                     page='1',
                                                                                                     key='news',
                                                                                                     pk=pk)),
        InlineKeyboardButton('Добавить документ', callback_data=user_callback.get_detail_callback(action='add_doc',
                                                                                                             pk=pk))
    ).add(
        InlineKeyboardButton(text='Назад', callback_data=user_callback.get_list_callback(action=action,
                                                                                                    page=page,
                                                                                                    key=key))
    )
    return markup


async def get_keyboard_for_flat(key: str, page: str, action: str, pk: int,
                                house_pk: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Забронировать',
                             callback_data=user_callback.get_detail_callback(action='booking_flat',
                                                                             pk=pk))
    ).add(
        InlineKeyboardButton(text='Назад', callback_data=user_callback.LIST_CB_WITH_PK.new(action=action,
                                                                                                      page=page,
                                                                                                      key=key,
                                                                                                      pk=house_pk))
    )
    return markup


async def get_keyboard_for_flat_list(items: Iterable, pages: dict, key: str,
                                     detail_action: str, list_action: str, pk: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=4)
    for index, item in enumerate(items, start=1):
        markup.insert(
            InlineKeyboardButton(text=f'{index}',
                                 callback_data=user_callback.get_detail_callback_with_page(action=detail_action,
                                                                                           pk=item.pk,
                                                                                           page=pages.get('current'),
                                                                                           key=key))
        )
    markup.add(
        InlineKeyboardButton(text='Назад', callback_data=user_callback.LIST_CB_WITH_PK.new(action=list_action,
                                                                                                      page=pages.get('prev'),
                                                                                                      key=key,
                                                                                                      pk=pk)),
        InlineKeyboardButton(text='Новое',
                             callback_data=user_callback.LIST_CB_WITH_PK.new(action=list_action,
                                                                             page=pages.get('first'),
                                                                             key=key,
                                                                             pk=pk)),
        InlineKeyboardButton(text='Вперед', callback_data=user_callback.LIST_CB_WITH_PK.new(action=list_action,
                                                                                                       page=pages.get('next'),
                                                                                                       key=key,
                                                                                                       pk=pk))
    )

    return markup


async def get_keyboard_for_my_flat(key: str, page: str, action: str, pk: int, house_pk: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('Редактировать', callback_data=user_callback.get_detail_callback(action='edit_flat',
                                                                                                         pk=pk))
    ).add(
        InlineKeyboardButton('Удалить', callback_data=user_callback.get_detail_callback(action='delete_flat',
                                                                                                   pk=pk))
    ).add(
        InlineKeyboardButton(text='Назад', callback_data=user_callback.LIST_CB_WITH_PK.new(action=action,
                                                                                                      page=page,
                                                                                                      key=key,
                                                                                                      pk=house_pk))
    )
    return markup


async def get_keyboard_for_booked_flat(key: str, page: str, action: str, pk: int,
                                       house_pk: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Отменить бронь',
                             callback_data=user_callback.get_detail_callback(action='unbooking_flat',
                                                                             pk=pk)),
        InlineKeyboardButton(text='Дом',
                             callback_data=user_callback.get_detail_callback_with_page(action='from_flat_house_detail',
                                                                                       pk=house_pk,
                                                                                       page=page,
                                                                                       key=key))
    ).add(
        InlineKeyboardButton(text='Назад', callback_data=user_callback.LIST_CB_WITH_PK.new(action=action,
                                                                                                      page=page,
                                                                                                      key=key,
                                                                                                      pk=house_pk))
    )
    return markup


async def get_keyboard_for_flat_detail_house(key: str, page: str, action: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Назад', callback_data=user_callback.LIST_CB_WITH_PK.new(action=action,
                                                                                                      page=page,
                                                                                                      key=key,
                                                                                                      pk='1'))
    )
    return markup


edit_user_role_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Клиент', callback_data=user_callback.POST_FILTER_CB.new(action='edit_role',
                                                                                             value='USER')),
    InlineKeyboardButton('Агент', callback_data=user_callback.POST_FILTER_CB.new(action='edit_role',
                                                                                            value='AGENT')),
    InlineKeyboardButton('Нотариус', callback_data=user_callback.POST_FILTER_CB.new(action='edit_role',
                                                                                               value='NOTARY')),
    InlineKeyboardButton('Отдел продаж', callback_data=user_callback.POST_FILTER_CB.new(action='edit_role',
                                                                                                   value='DEPART')),
)


async def get_keyboard_for_document_detail(pk: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton('Удалить', callback_data=user_callback.DETAIL_WITH_PAGE_CB.new(action='delete_house_structure',
                                                                                                       key='documents',
                                                                                                       page='1',
                                                                                                       pk=pk))
    )


async def get_keyboard_for_request_detail(pk: int, page: str, key: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton('Одобрить', callback_data=user_callback.get_detail_callback_with_page(action='approve_request',
                                                                                                              page=page,
                                                                                                              key=key,
                                                                                                              pk=pk)),
        InlineKeyboardButton('Отказать',
                             callback_data=user_callback.get_detail_callback_with_page(action='disapprove_request',
                                                                                       page=page,
                                                                                       key=key,
                                                                                       pk=pk))
    ).add(
        InlineKeyboardButton('Назад', callback_data=user_callback.get_list_callback(action='request_list',
                                                                                               page=page,
                                                                                               key=key))
    )


async def get_keyboard_for_notary_list(pk: int, page: str, key: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton('Убрать из списка нотариусов',
                             callback_data=user_callback.get_detail_callback_with_page(action='remove_from_notary',
                                                                                       page=page,
                                                                                       key=key,
                                                                                       pk=pk))
    ).add(
        InlineKeyboardButton('Назад', callback_data=user_callback.get_list_callback(action='user_notary_list',
                                                                                               page=page,
                                                                                               key=key))
    )


async def get_keyboard_for_complaint_list(pk: int, page: str, key: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton('Одобрить',
                             callback_data=user_callback.get_detail_callback_with_page(action='approve_complaint',
                                                                                       page=page,
                                                                                       key=key,
                                                                                       pk=pk)),
        InlineKeyboardButton('Отказать',
                             callback_data=user_callback.get_detail_callback_with_page(action='disapprove_complaint',
                                                                                       page=page,
                                                                                       key=key,
                                                                                       pk=pk))
    ).add(
        InlineKeyboardButton(translate('Назад'), callback_data=user_callback.get_list_callback(action='complaint_list',
                                                                                               page=page,
                                                                                               key=key))
    )
