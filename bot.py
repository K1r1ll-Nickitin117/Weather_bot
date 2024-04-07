# import logging
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Bot:
    @dp.message(Command(commands=["start"]))
    async def process_start_command(self, message: Message):
        await message.answer('in start')

    @dp.message(Command(commands=['help']))
    async def process_help_command(self, message: Message):
        await message.answer('in help')

    @dp.message()
    async def send_echo(self, message: Message):
        await message.reply(text='Я пока такое не умею обрабатывать)')


if __name__ == 'main':
    dp.run_polling(bot)
    