from aiogram import Router
from aiogram.types import Message
from stone_knots_paper_bot.lexicon.lexicon import LEXICON_RU

router = Router()


@router.message()
async def process_invite_again(message: Message):
    await message.answer(text=LEXICON_RU['no_understand'])
