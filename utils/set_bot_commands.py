from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", 'Запустить бота'),
            types.BotCommand("admin", 'Панель администратора'),
            types.BotCommand("help", 'Вывести справку'),
            types.BotCommand("cancel", 'Отменить/Пропустить')
        ]
    )