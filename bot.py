from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types
from aiogram import Bot
from set_menu import set_main_menu
from config import BOT_TOKEN
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)


class Bot:
    @dp.message(Command(commands=["start"]))
    async def process_start_command(message: Message):
        await message.answer('start')

    @dp.message(Command(commands=['help']))
    async def process_help_command(self, message: Message):
        await set_main_menu(bot)
        await message.answer('help')

    @dp.message(Command(commands=['location_now']))
    async def process_location_now_command(self, message: Message):
        await message.answer('location_now')

    @dp.message(Command(commands=['weather']))
    async def process_weather_command(self, message: Message):
        await message.answer('weather')

    @dp.message(Command(commands=['my_location']))
    async def process_my_location_command(self, message: Message):
        await message.answer('my_location')

    @dp.message(Command(commands=['change_location']))
    async def process_change_location_command(self, message: Message):
        await message.answer('change_location')

    @dp.message(Command(commands=['what_to_wear']))
    async def process_what_to_wear_command(self, message: Message):
        await message.answer('what_to_wear')

    @dp.message()
    async def send_echo(self, message: Message):
        await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
