from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(
    keyboard=[
            [types.KeyboardButton(text='/location_now'), types.KeyboardButton(text='/weather')],
            [types.KeyboardButton(text='/my_location'), types.KeyboardButton(text='/change_location')],
            [types.KeyboardButton(text='/what_to_wear'), types.KeyboardButton(text='/help')],
            [types.KeyboardButton(text='/start'), types.KeyboardButton(text='/restart')]
        ],
    resize_keyboard=True
)
