from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Погода'), types.KeyboardButton(text='Статистика')],
        [types.KeyboardButton(text='Рестарт'), types.KeyboardButton(text='Справка')],
        [types.KeyboardButton(text='О проекте')]

    ],
    resize_keyboard=True
)
