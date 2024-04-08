import logging

from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, F, types

from settings.set_menu import set_menu
from settings.keyboard import main_kb
from settings.phrases import (help_phrase,
                              start_phrase,
                              location_now_phrase,
                              weather_phrase,
                              my_location_phrase,
                              change_location_phrase,
                              what_to_wear_phrase,
                              restart_phrase,
                              if_the_message_has_not_been_processed_phrase)

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)

logging.basicConfig(level=logging.INFO)


class Bot:

    @dp.message(CommandStart())
    async def process_start_command(message: Message):
        await message.answer(f'Привет, {message.from_user.first_name}' + ' ' + start_phrase, reply_markup=main_kb)
        await set_menu(bot)

    @dp.message(F.text == 'Справка')
    async def process_help_command(message: Message):
        await message.answer(help_phrase)

    @dp.message(F.text == 'Локация сейчас')
    async def process_location_now_command(message: Message):
        await message.answer(location_now_phrase)

    @dp.message(F.text == 'Погода')
    async def process_weather_command(message: Message):
        await message.answer(weather_phrase)

    @dp.message(F.text == 'Моя локация')
    async def process_my_location_command(message: Message):
        await message.answer(my_location_phrase)

    @dp.message(F.text == 'Сменить локацию')
    async def process_change_location_command(message: Message):
        await message.answer(change_location_phrase)

    @dp.message(F.text == 'Что надеть')
    async def process_what_to_wear_command(message: Message):
        await message.answer(what_to_wear_phrase)

    @dp.message()
    async def send_echo(message: Message):
        await message.reply(if_the_message_has_not_been_processed_phrase)


if __name__ == '__main__':
    dp.run_polling(bot)
