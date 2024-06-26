import logging
import json
import os

from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F, types

# from giga_chat_api.gigachat_api import giga_chat_weather
from settings.urlkb import inlkb
from check_city import check_city
from db.db_s import DB
from api_open_weather.find_location import find_location
from settings.set_menu import set_menu
from settings.keyboard import main_kb
from settings.phrases import (help_phrase,
                              start_phrase,
                              weather_phrase,
                              restart_phrase,
                              if_the_message_has_not_been_processed_phrase,
                              is_city_false)

from settings.config import BOT_TOKEN

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

    @dp.message(F.text == 'Рестарт')
    async def process_restart_command(message: Message):
        db = DB()
        db.drop_table()
        await message.answer(restart_phrase)

    @dp.message(F.text == 'О проекте')
    async def url_command(message: types.Message):
        await message.answer(
            text='О проекте:',
            reply_markup=inlkb
        )

    @dp.message(Command(commands=['about']))
    async def url_command_s(message: types.Message):
        await message.answer(
            text='О проекте:',
            reply_markup=inlkb
        )

    @dp.message(F.text == 'Статистика')
    async def process_stat_command(message: Message):
        db = DB()
        await message.answer(db.get_stat())

    @dp.message(Command(commands=['weather']))
    async def weather_command(message: Message):
        await message.answer(weather_phrase)

    @dp.message(F.text)
    async def get_city_name(message: types.Message):
        city_name = message.text
        is_city = check_city(city_name)
        if is_city:
            await find_location(city_name)
            with open('data/weather.json', 'r', encoding='utf-8') as weather:
                weather_data = json.load(weather)
            description = weather_data['weather'][0]['description']
            temp_min = weather_data['main']['temp_min']
            temp_max = weather_data['main']['temp_max']
            feels_like = weather_data['main']['feels_like']
            ans = f'''Погода в месте {city_name}:\n
Описание - {description}.\n
Минимальная температура: {int(temp_min - 273.15)} градусов.\n
Минимальная максимальная: - {int(temp_max - 273.15)} градусов.\n
Ошущается как: {int(feels_like - 273.15)} градусов.\n
    '''
            await message.answer(ans)
            # await message.answer(giga_chat_weather(ans))

            with open('data/find_location.json', 'r', encoding='utf-8') as cooords:
                data = json.load(cooords)

            db = DB()
            db.add_city(city_name, float(data[0]['lat']), float(data[0]['lon']))

            if os.path.exists('data/find_location.json'):
                os.remove('data/find_location.json')
            if os.path.exists('data/weather.json'):
                os.remove('data/weather.json')
            if os.path.exists('data/check_city.json'):
                os.remove('data/check_city.json')

        else:
            await message.answer(is_city_false)

    @dp.message(Command(commands=['help']))
    async def help_command(message: Message):
        await message.answer(help_phrase)

    @dp.message(Command(commands=['about']))
    async def about_command(message: Message):
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
