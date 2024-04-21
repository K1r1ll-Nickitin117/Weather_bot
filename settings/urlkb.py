from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

dev = InlineKeyboardButton(
    text='Разработчик',
    url='https://t.me/Coder_k1r1ll'
)
github = InlineKeyboardButton(
    text='GitHub проекта',
    url='https://github.com/K1r1ll-Nickitin117/Weather_bot'
)

inlkb = InlineKeyboardMarkup(
    inline_keyboard=[[dev],
                     [github]]
)
