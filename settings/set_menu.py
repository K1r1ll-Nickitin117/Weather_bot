from aiogram import Bot
from aiogram.types import BotCommand


COMMANDS: dict[str, str] = {
    '/weather': 'Погода',
    '/what_to_wear': 'Что надеть',
    '/help': 'Справка по боту',
    '/start': 'Старт бота',
    '/restart': 'Рестарт бота'
}


async def set_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in COMMANDS.items()
    ]
    await bot.set_my_commands(main_menu_commands)
