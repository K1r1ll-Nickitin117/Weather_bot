from aiogram import Bot, Dispatcher, types

kb = [
            [types.KeyboardButton(text='Локация сейчас'), types.KeyboardButton(text='Погода')],
            [types.KeyboardButton(text='Мои локации'), types.KeyboardButton(text='Поменять локацию')],
            [types.KeyboardButton(text='Что надеть'), types.KeyboardButton(text='Помощь')]
        ]

keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
