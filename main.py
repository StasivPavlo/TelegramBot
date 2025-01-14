from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("fffffff")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg == 'hello':
        await msg.reply("world")
    elif msg == 'world':
        await msg.reply("hello")
    else:
        await msg.reply("error")




if __name__ == '__main__':
    executor.start_polling(dp)