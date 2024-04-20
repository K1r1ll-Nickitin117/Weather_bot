import logging
import json
import os

from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F, types

from db.db_s import DB
from api_open_weather.find_location import find_location
from settings.set_menu import set_menu
from settings.keyboard import main_kb
from settings.phrases import (help_phrase,
                              start_phrase,
                              weather_phrase,
                              what_to_wear_phrase,
                              restart_phrase,
                              if_the_message_has_not_been_processed_phrase)

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)


class Bot(DB):
    def __init__(self):
        super.__init__()

    @dp.message(CommandStart())
    async def process_start_command(message: Message):
        await message.answer(f'Привет, {message.from_user.first_name}' + ' ' + start_phrase, reply_markup=main_kb)
        await set_menu(bot)

    @dp.message(F.text == 'Справка')
    async def process_help_command(message: Message):
        await message.answer(help_phrase)

    @dp.message(F.text == 'Погода')
    async def process_weather_command(message: Message):
        await message.answer(weather_phrase)

    @dp.message(F.text == 'Что надеть')
    async def process_what_to_wear_command(message: Message):
        await message.answer(what_to_wear_phrase)

    @dp.message(F.text == 'Рестарт')
    async def process_restart_command(message: Message):
        db = DB()
        db.drop_table()
        await message.answer(restart_phrase)

    @dp.message(F.text == 'Статистика')
    async def process_stat_command(message: Message):
        db = DB()
        await message.answer(db.get_stat())

    @dp.message(Command(commands=['weather']))
    async def weather_command(message: Message):
        await message.answer(weather_phrase)

    @dp.message(lambda x: x.text and x.text.istitle())
    async def get_city_name(message: types.Message):
        city_name = message.text
        await find_location(city_name)
        with open('data/weather.json', 'r', encoding='utf-8') as weather:
            weather_data = json.load(weather)
        description = weather_data['weather'][0]['description']
        temp_min = weather_data['main']['temp_min']
        temp_max = weather_data['main']['temp_max']
        feels_like = weather_data['main']['feels_like']
        await message.answer(f'''Погода в месте {city_name}:\n
Описание - {description}.\n
Минимальная температура: {int(temp_min - 273.15)} градусов.\n
Минимальная максимальная: - {int(temp_max - 273.15)} градусов.\n
Ошущается как: {int(feels_like - 273.15)} градусов.\n
                           ''')

        with open('data/find_location.json', 'r', encoding='utf-8') as cooords:
            data = json.load(cooords)

        db = DB()
        db.add_city(city_name, float(data[0]['lat']), float(data[0]['lon']))

        os.remove('data/find_location.json')
        os.remove('data/weather.json')

    @dp.message(Command(commands=['what_to_wear']))
    async def what_to_wear_command(message: Message):
        await message.answer(what_to_wear_phrase)

    @dp.message(Command(commands=['help']))
    async def help_command(message: Message):
        await message.answer(help_phrase)

    @dp.message(Command(commands=['restart']))
    async def restart_command(message: Message):
        db = DB()
        db.drop_table()
        await message.answer(restart_phrase)

    @dp.message(Command(commands=['stat']))
    async def stat_command(message: Message):
        db = DB()
        await message.answer(db.get_stat())

    @dp.message()
    async def if_the_message_has_not_been_processed(message: Message):
        await message.reply(if_the_message_has_not_been_processed_phrase)


if __name__ == '__main__':
    dp.run_polling(bot)
