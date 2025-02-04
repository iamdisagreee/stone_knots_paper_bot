from aiogram import Bot
from aiogram.types import BotCommand

from stone_knots_paper_bot.lexicon.lexicon import LEXICON_RU


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command='/start',
            description='Начало игры'
        ),
        BotCommand(
            command='/help',
            description='Справка по работе бота'
        )
    ]
    await bot.set_my_commands(main_menu_commands)

# # Этот хэндлер будет срабатывать на команду "/delmenu"
# # и удалять кнопку Menu c командами
# @dp.message(Command(commands='delmenu'))
# async def del_main_menu(message: Message, bot: Bot):
#     await bot.delete_my_commands()
#     await message.answer(text='Кнопка "Menu" удалена')