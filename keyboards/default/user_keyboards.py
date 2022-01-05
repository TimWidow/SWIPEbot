from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_user_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Список публикаций'),
        KeyboardButton('Список домов')
    ).row(
        KeyboardButton('Избранное')
    ).row(
        KeyboardButton('Входящие запросы на добавление в шахматку')
    ).row(
        KeyboardButton('Настройки')
    )
    return markup


async def get_level_2_post_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Вернуться'),
    ).add(
        KeyboardButton('Фильтрация объявлений')
    ).add(
        KeyboardButton('Текущие фильтры'),
        KeyboardButton('Мои фильтры'),
        KeyboardButton('Сбросить фильтры')
    ).add(
        KeyboardButton('Добавить новую публикацию'),
        KeyboardButton('Мои объявления')
    )
    return markup


async def get_level_2_filter_post_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Фильтровать')
    ).add(
        KeyboardButton('Перейти к цене')
    ).add(
        KeyboardButton('Перейти к площади')
    ).add(
        KeyboardButton('Перейти к городу')
    ).add(
        KeyboardButton('Перейти к состоянию квартиры')
    ).add(
        KeyboardButton('Перейти к планировке')
    ).add(
        KeyboardButton('Перейти к территории')
    ).add(
        KeyboardButton('Вернуться'),
        KeyboardButton('Сохранить фильтр')
    )
    return markup


async def get_level_3_create_post_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Сохранить')
    ).add(
        KeyboardButton('Перейти к дому'),
        KeyboardButton('Перейти к квартире')
    ).add(
        KeyboardButton('Перейти к цене'),
        KeyboardButton('Перейти к способу платежа')
    ).add(
        KeyboardButton('Перейти к вариантам связи')
    ).add(
        KeyboardButton('Перейти к описанию'),
        KeyboardButton('Перейти к фото')
    ).add(
        KeyboardButton('Вернуться')
    )
    return markup


async def get_level_2_house_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Все дома')
    ).add(
        KeyboardButton('Мои квартиры'),
        KeyboardButton('Мои дома')
    ).add(
        KeyboardButton('Вернуться')
    )
    return markup


async def get_level_3_my_house_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Добавить дом')
    ).add(
        KeyboardButton('Вернуться')
    )
    return markup


async def get_level_4_create_house() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton('Сохранить')
    ).add(
        KeyboardButton('Перейти к названию'),
        KeyboardButton('Перейти к городу'),
        KeyboardButton('Перейти к адресу')
    ).add(
        KeyboardButton('Перейти к технологии строительства'),
        KeyboardButton('Перейти к территории')
    ).add(
        KeyboardButton('Перейти к платежным способами'),
        KeyboardButton('Перейти к описанию')
    ).add(
        KeyboardButton('Перейти к статусу'),
        KeyboardButton('Перейти к типу'),
        KeyboardButton('Перейти к классу дома'),
    ).add(
        KeyboardButton('Перейти к расстоянию до моря'),
        KeyboardButton('Перейти к высоте потолков')
    ).add(
        KeyboardButton('Перейти к газопроводу'),
        KeyboardButton('Перейти к отоплению'),
        KeyboardButton('Перейти к электричеству'),
        KeyboardButton('Перейти к канализации'),
        KeyboardButton('Перейти к водоснабжению')
    ).add(
        KeyboardButton('Перейти к спортивной площадке'),
        KeyboardButton('Перейти к парковке'),
        KeyboardButton('Перейти к магазину'),
        KeyboardButton('Перейти к детской площадке'),
        KeyboardButton('Перейти к лифту'),
        KeyboardButton('Перейти к охране')
    ).add(
        KeyboardButton('Перейти к картинке')
    ).add(
        KeyboardButton('Вернуться')
    )
    return markup


async def get_level_2_user_settings_keyboard(is_admin=None) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Изменить данные'),
        KeyboardButton('Настройки подписки'),
        KeyboardButton('Язык')
    )
    if is_admin:
        markup.add(
            KeyboardButton('Отключить режим администратора')
        )
    else:
        markup.add(
            KeyboardButton('Ввести токен администратора')
        )
    markup.add(
        KeyboardButton('Вернуться')
    )
    return markup


async def get_level_2_admin_panel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Список нотариусов'),
        KeyboardButton('Жалобы')
    ).add(
        KeyboardButton('Рассылка')
    ).add(
        KeyboardButton('Получить логи'),
        KeyboardButton('Получить список пользователей'),
    ).add(
        KeyboardButton('Восстановить пользователей через json')
    ).add(
        KeyboardButton('Вернуться')
    )


async def get_level_3_user_settings_edit_data() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Сохранить')
    ).add(
        KeyboardButton('Перейти к имени и фамилии'),
        KeyboardButton('Перейти к электронной почте')
    ).add(
        KeyboardButton('Перейти к фото'),
        KeyboardButton('Перейти к роли')
    ).add(
        KeyboardButton('Вернуться')
    )


async def get_level_3_user_subscription_settings() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Получить подписку'),
        KeyboardButton('Проверить статус подписки')
    ).add(
        KeyboardButton('Вернуться')
    ).add(
        KeyboardButton('Отменить подписку')
    )


async def get_level_3_add_promotion() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Сохранить')
    ).add(
        KeyboardButton('Перейти к фразе'),
        KeyboardButton('Перейти к типу')
    ).add(
        KeyboardButton('Вернуться')
    )


async def get_level_4_add_flat() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Сохранить')
    ).add(
        KeyboardButton('Перейти к этажу')
    ).add(
        KeyboardButton('Перейти к номеру'),
        KeyboardButton('Перейти к площади'),
        KeyboardButton('Перейти к площади кухи')
    ).add(
        KeyboardButton('Перейти к цене'),
        KeyboardButton('Перейти к цене за кв. метр'),
        KeyboardButton('Перейти к числу комнат')
    ).add(
        KeyboardButton('Перейти к состоянию'),
        KeyboardButton('Перейти к типу собственности'),
    ).add(
        KeyboardButton('Перейти к типу'),
        KeyboardButton('Перейти к балкону'),
        KeyboardButton('Перейти к отоплению')
    ).add(
        KeyboardButton('Перейти к схеме')
    ).add(
        KeyboardButton('Вернуться')
    )


async def get_level_4_add_news() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Сохранить')
    ).add(
        KeyboardButton('Перейти к заголовку'),
        KeyboardButton('Перейти к описанию')
    ).add(
        KeyboardButton('Вернуться')
    )


async def get_level_4_add_doc() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Сохранить')
    ).add(
        KeyboardButton('Перейти к названию'),
        KeyboardButton('Перейти к файлу')
    ).add(
        KeyboardButton('Вернуться')
    )


async def get_restore_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Вернуться')
    )
