from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.callbacks.user_callback import POST_FILTER_CB


ITEM_CB = POST_FILTER_CB


phrase_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Подарок при покупке', callback_data=ITEM_CB.new(action='add_phrase',
                                                                          value='GIFT')),
    InlineKeyboardButton('Возможен торг', callback_data=ITEM_CB.new(action='add_phrase',
                                                                    value='TRADE'))
    ).add(
    InlineKeyboardButton('Квартира у моря', callback_data=ITEM_CB.new(action='add_phrase',
                                                                      value='SEA')),
    InlineKeyboardButton('В спальном районе', callback_data=ITEM_CB.new(action='add_phrase',
                                                                        value='SLEEP'))
).add(
    InlineKeyboardButton('Вам повезло с ценой', callback_data=ITEM_CB.new(action='add_phrase',
                                                                          value='PRICE')),
    InlineKeyboardButton('Для большой семьи', callback_data=ITEM_CB.new(action='add_phrase',
                                                                        value='BIG_FAMILY'))
).add(
    InlineKeyboardButton('Семейное гнёздышко', callback_data=ITEM_CB.new(action='add_phrase',
                                                                         value='FAMILY')),
    InlineKeyboardButton('Отдельная парковка', callback_data=ITEM_CB.new(action='add_phrase',
                                                                         value='CAR_PARK'))
)


async def get_promotion_type_keyboard(items: list) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for item in items:
        markup.insert(
            InlineKeyboardButton(item['name'], callback_data=ITEM_CB.new(action='add_type',
                                                                         value=item['id']))
        )
    return markup
