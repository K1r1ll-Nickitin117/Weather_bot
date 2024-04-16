import logging
import json
from translate import Translator
import os

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F, types, Router


from api_open_weather.find_location import find_location, get_weather
from settings.set_menu import set_menu
from settings.keyboard import main_kb
from settings.phrases import (help_phrase,
                              start_phrase,
                              weather_phrase,
                              what_to_wear_phrase,
                              restart_phrase,
                              if_the_message_has_not_been_processed_phrase)

from config import BOT_TOKEN

to_ru = Translator(to_lang="Ru")
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)


class Bot():
    @dp.message(CommandStart())
    async def process_start_command(message: Message):
        await message.answer(f'Привет, {message.from_user.first_name}' + ' ' + start_phrase, reply_markup=main_kb)
        await set_menu(bot)

    @dp.message(F.text == 'Справка')  # Здесь работа закочена
    async def process_help_command(message: Message):
        await message.answer(help_phrase)

    @dp.message(F.text == 'Погода')
    async def process_weather_command(message: Message):
        await message.answer(weather_phrase)

    @dp.message(F.text == 'Что надеть')
    async def process_what_to_wear_command(message: Message):
        await message.answer(what_to_wear_phrase)

    @dp.message(F.text == 'Рестарт')
    async def process_help_command(message: Message):
        await message.answer(restart_phrase)

    @dp.message(Command(commands=['weather']))
    async def weather_command(message: Message):
        await message.answer(weather_phrase)

    @dp.message()
    async def get_city_name(message: types.Message, state: FSMContext):
        city_name = message.text
        await find_location(city_name)
        with open('data/weather.json', 'r', encoding='utf-8') as weather:
            weather_data = json.load(weather)
        description = weather_data['weather'][0]['description']
        temp_min = weather_data['main']['temp_min']
        temp_max = weather_data['main']['temp_max']
        feels_like = weather_data['main']['feels_like']
        await message.answer(f'''Погода в месте {city_name}:\n
    Описание - {to_ru.translate(description)}.\n
    Минимальная температура: {int(temp_min - 273.15)} градусов.\n
    Минимальная максимальная: - {int(temp_max - 273.15)} градусов.\n
    Ошущается как: {int(feels_like - 273.15)} градусов.\n
                           ''')
        os.remove('data/find_location.json')
        os.remove('data/weather.json')

    @dp.message(Command(commands=['what_to_wear']))
    async def what_to_wear_command(message: Message):
        await message.answer(what_to_wear_phrase)

    @dp.message(Command(commands=['help']))  # Здесь работа закончена
    async def help_command(message: Message):
        await message.answer(help_phrase)

    @dp.message(Command(commands=['restart']))
    async def restart_command(message: Message):
        await message.answer(restart_phrase)

    @dp.message()
    async def send_echo(message: Message):
        await message.reply(if_the_message_has_not_been_processed_phrase)


if __name__ == '__main__':
    dp.run_polling(bot)
