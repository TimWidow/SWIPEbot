from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.callbacks.user_callback import POST_FILTER_CB, get_detail_callback_with_page

ITEM_CB = POST_FILTER_CB

tech_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Монолитный каркас с керамзитно-блочным заполнением',
                         callback_data=ITEM_CB.new(action='add_tech',
                                                   value='MONO1')),
    InlineKeyboardButton('Монолитно-кирпичный',
                         callback_data=ITEM_CB.new(action='add_tech',
                                                   value='MONO2')),
    InlineKeyboardButton('Монолитно-каркасный',
                         callback_data=ITEM_CB.new(action='add_tech',
                                                   value='MONO3'))
).row(
    InlineKeyboardButton('Панельный',
                         callback_data=ITEM_CB.new(action='add_tech',
                                                   value='PANEL')),
    InlineKeyboardButton('Пеноблок',
                         callback_data=ITEM_CB.new(action='add_tech',
                                                   value='FOAM')),
    InlineKeyboardButton('Газобетон',
                         callback_data=ITEM_CB.new(action='add_tech',
                                                   value='AREATED'))
)

terr_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Открытая', callback_data=ITEM_CB.new(action='add_terr',
                                                               value='OPEN')),
    InlineKeyboardButton('Закрытая', callback_data=ITEM_CB.new(action='add_terr',
                                                               value='CLOSE'))
)

payment_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Ипотека', callback_data=ITEM_CB.new(action='add_payment',
                                                              value='MORTGAGE')),
    InlineKeyboardButton('Материнский капитал', callback_data=ITEM_CB.new(action='add_payment',
                                                                          value='CAPITAL')),
    InlineKeyboardButton('Прямая оплата', callback_data=ITEM_CB.new(action='add_payment',
                                                                    value='PAYMENT'))
)

role_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Квартиры', callback_data=ITEM_CB.new(action='add_role',
                                                               value='FLAT')),
    InlineKeyboardButton('Офисы', callback_data=ITEM_CB.new(action='add_role',
                                                            value='OFFICE'))
)

type_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Многоквартирный', callback_data=ITEM_CB.new(action='add_type',
                                                                      value='MANY')),
    InlineKeyboardButton('Частный', callback_data=ITEM_CB.new(action='add_type',
                                                              value='ONE'))
).add(
    InlineKeyboardButton('Новострой', callback_data=ITEM_CB.new(action='add_type',
                                                                value='NOVOSTROY')),
    InlineKeyboardButton('Вторичный рынок', callback_data=ITEM_CB.new(action='add_type',
                                                                      value='SECONDARY')),
    InlineKeyboardButton('Коттеджи', callback_data=ITEM_CB.new(action='add_type',
                                                               value='COTTAGES'))
)

house_class_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Обычный', callback_data=ITEM_CB.new(action='add_house_class',
                                                              value='COMMON')),
    InlineKeyboardButton('Элитный', callback_data=ITEM_CB.new(action='add_house_class',
                                                              value='ELITE'))
)

gas_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Нет', callback_data=ITEM_CB.new(action='add_gas',
                                                          value='NO')),
    InlineKeyboardButton('Централизованный', callback_data=ITEM_CB.new(action='add_gas',
                                                                       value='CENTER'))
)

heating_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Нет', callback_data=ITEM_CB.new(action='add_heating',
                                                          value='NO')),
    InlineKeyboardButton('Центральное', callback_data=ITEM_CB.new(action='add_heating',
                                                                  value='CENTER')),
    InlineKeyboardButton('Индивидуальное', callback_data=ITEM_CB.new(action='add_heating',
                                                                     value='PERSONAL'))
)

electricity_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Нет', callback_data=ITEM_CB.new(action='add_electricity',
                                                          value='NO')),
    InlineKeyboardButton('Подключено', callback_data=ITEM_CB.new(action='add_electricity',
                                                                 value='YES'))
)

sewerage_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Нет', callback_data=ITEM_CB.new(action='add_sewerage',
                                                          value='NO')),
    InlineKeyboardButton('Центральная', callback_data=ITEM_CB.new(action='add_sewerage',
                                                                  value='CENTRAL')),
    InlineKeyboardButton('Индивидуальная', callback_data=ITEM_CB.new(action='add_sewerage',
                                                                     value='PERSONAL'))
)

water_supply_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Нет', callback_data=ITEM_CB.new(action='add_water',
                                                          value='NO')),
    InlineKeyboardButton('Центральное', callback_data=ITEM_CB.new(action='add_water',
                                                                  value='CENTRAL')),
    InlineKeyboardButton('Индивидуальное', callback_data=ITEM_CB.new(action='add_water',
                                                                     value='PERSONAL'))
)

confirm_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Да', callback_data=ITEM_CB.new(action='create_confirm',
                                                         value=True)),
    InlineKeyboardButton('Нет', callback_data=ITEM_CB.new(action='create_confirm',
                                                          value=False))
)


async def get_advantages_keyboard(action: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton('Есть', callback_data=ITEM_CB.new(action=action,
                                                               value=True)),
        InlineKeyboardButton('Нет', callback_data=ITEM_CB.new(action=action,
                                                              value=False))
    )


#  Block, Section, Floor, Standpipe
async def get_building_keyboard(action: str, items: list, key: str, page: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for index, item in enumerate(items, start=1):
        markup.insert(InlineKeyboardButton(str(index), callback_data=get_detail_callback_with_page(action=action,
                                                                                                   pk=item['id'],
                                                                                                   key=key,
                                                                                                   page=page)))
    return markup
