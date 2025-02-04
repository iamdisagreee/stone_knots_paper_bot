import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from stone_knots_paper_bot.handlers import user_handlers, other_handlers
from stone_knots_paper_bot.keyboards.set_menu import set_main_menu


async def main() -> None:
    config = load_config()

    bot = Bot(token=config.tgBot.token)
    dp = Dispatcher()
    await set_main_menu(bot)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
