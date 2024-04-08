import logging

from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types

from settings.set_menu import set_main_menu
from settings.keyboard import keyboard
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)

logging.basicConfig(level=logging.INFO)


class Bot:
    @dp.message(CommandStart())
    async def process_start_command(message: Message):
        await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь', reply_markup=keyboard)

    @dp.message(Command(commands=['help']))
    async def process_help_command(message: Message):
        await message.answer(
            'Напиши мне что-нибудь и в ответ '
            'я пришлю тебе твое сообщение'
        )

    @dp.message(Command(commands=['location_now']))
    async def process_location_now_command(message: Message):
        await message.answer('location_now')

    @dp.message(Command(commands=['weather']))
    async def process_weather_command(message: Message):
        await message.answer('weather')

    @dp.message(Command(commands=['my_location']))
    async def process_my_location_command(message: Message):
        await message.answer('my_location')

    @dp.message(Command(commands=['change_location']))
    async def process_change_location_command(message: Message):
        await message.answer('change_location')

    @dp.message(Command(commands=['what_to_wear']))
    async def process_what_to_wear_command(message: Message):
        await message.answer('what_to_wear')

    @dp.message()
    async def send_echo(message: Message):
        await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
