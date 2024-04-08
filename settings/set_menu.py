from aiogram import Bot
from aiogram.types import BotCommand


COMMANDS: dict[str, str] = {
    '/location_now': 'Локация сейчас',
    '/weather': 'Погода',
    '/my_location': 'Мои локации',
    '/change_location': 'Поменять локацию',
    '/what_to_wear': 'Что надеть',
    '/help': 'Помощь'
}


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in COMMANDS.items()
    ]
    await bot.set_my_commands(main_menu_commands)
