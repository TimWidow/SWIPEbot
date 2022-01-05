from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = 'SWIPEbot поможет вам получить информацию об актуальных предложениях аренды'

    await message.answer(text)
