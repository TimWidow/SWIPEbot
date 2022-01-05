from aiogram import executor
from filters.admin import IsAdmin
from loader import dp, Conn, db, TORTOISE_ORM
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import middlewares, filters, handlers


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await db.init(config=TORTOISE_ORM)
    await db.generate_schemas()
    dp.filters_factory.bind(IsAdmin)
    await on_startup_notify(dispatcher)


async def on_shutdown():
    await db.close_connections()
    await Conn.close()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
