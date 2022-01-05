from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.callbacks.user_callback import POST_FILTER_CB

labels = {
    'BLANK': 'После ремонта',
    'ROUGH': 'Черновая',
    'EURO': 'Евроремонт',
    'NEED': 'Требует ремонта',
    'OPEN': 'Открытая',
    'CLOSE': 'Закрытая',
    'FREE': 'Свободная планировка',
    'STUDIO': 'Студия',
    'ADJACENT': 'Смежные комнаты',
    'ISOLATED': 'Изолированные комнаты',
    'SMALL': 'Малосемейка',
    'ROOM': 'Гостинка'
}


async def get_filter_post_state_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text=translate('После ремонта'), callback_data=POST_FILTER_CB.new(action='filter_state',
                                                                                               value='BLANK')),
        InlineKeyboardButton(text=translate('Черновая'), callback_data=POST_FILTER_CB.new(action='filter_state',
                                                                                          value='ROUGH'))
    ).add(
        InlineKeyboardButton(text=translate('Евроремонт'), callback_data=POST_FILTER_CB.new(action='filter_state',
                                                                                            value='EURO')),
        InlineKeyboardButton(text=translate('Требует ремонта'), callback_data=POST_FILTER_CB.new(action='filter_state',
                                                                                                 value='NEED'))
    )
    return markup


async def get_filter_post_territory_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text=translate('Открытая'), callback_data=POST_FILTER_CB.new(action='filter_territory',
                                                                                          value='OPEN')),
        InlineKeyboardButton(text=translate('Закрытая'), callback_data=POST_FILTER_CB.new(action='filter_territory',
                                                                                          value='CLOSE'))
    )
    return markup


async def get_filter_post_plan_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text=translate('Свободная планировка'),
                             callback_data=POST_FILTER_CB.new(action='filter_plan',
                                                              value='FREE')),
        InlineKeyboardButton(text=translate('Студия'), callback_data=POST_FILTER_CB.new(action='filter_plan',
                                                                                        value='STUDIO'))
    ).add(
        InlineKeyboardButton(text=translate('Смежные комнаты'), callback_data=POST_FILTER_CB.new(action='filter_plan',
                                                                                                 value='ADJACENT')),
        InlineKeyboardButton(text=translate('Изолированные комнаты'),
                             callback_data=POST_FILTER_CB.new(action='filter_plan',
                                                              value='ISOLATED'))
    ).add(
        InlineKeyboardButton(text=translate('Малосемейка'), callback_data=POST_FILTER_CB.new(action='filter_plan',
                                                                                             value='SMALL')),
        InlineKeyboardButton(text=translate('Гостинка'), callback_data=POST_FILTER_CB.new(action='filter_plan',
                                                                                          value='ROOM'))
    )
    return markup


async def get_filter_post_confirm_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text=translate('Подтверждаю'), callback_data=POST_FILTER_CB.new(action='filter_confirm',
                                                                                             value='YES')),
        InlineKeyboardButton(text=translate('Ещё подумаю'), callback_data=POST_FILTER_CB.new(action='filter_confirm',
                                                                                             value='NO'))
    )
    return markup
