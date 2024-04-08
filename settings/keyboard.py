from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Локация сейчас'), types.KeyboardButton(text='Погода')],
        [types.KeyboardButton(text='Моя локация'), types.KeyboardButton(text='Сменить локацию')],
        [types.KeyboardButton(text='Что надеть'), types.KeyboardButton(text='Справка')],
    ],
    resize_keyboard=True
)
