from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


starter_confirm = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Подтвердить')
)


async def get_contact_button() -> ReplyKeyboardMarkup:
    contact_button = KeyboardButton(text='Отправить номер телефона', request_contact=True)
    contact_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(contact_button)
    return contact_markup


async def get_skip_button() -> ReplyKeyboardMarkup:
    skip_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        KeyboardButton(text='Пропустить')
    )
    return skip_markup


remove_markup = ReplyKeyboardRemove()
