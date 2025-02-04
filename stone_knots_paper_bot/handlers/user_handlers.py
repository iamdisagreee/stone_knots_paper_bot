from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from stone_knots_paper_bot.lexicon.lexicon import LEXICON_RU
from stone_knots_paper_bot.keyboards.keyboards import yes_no_kb, game_kb
from stone_knots_paper_bot.services.services import random_stone_knots_paper, result_random

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=yes_no_kb)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=yes_no_kb)


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_start_game(message: Message):
    await message.answer(text=LEXICON_RU['do'],
                         reply_markup=game_kb)


@router.message(F.text == LEXICON_RU['no_button'])
async def process_start_game(message: Message):
    await message.answer(text=LEXICON_RU['no_do'])


@router.message(F.text.in_([LEXICON_RU['stone'],
                            LEXICON_RU['knots'],
                            LEXICON_RU['paper']]))
async def process_play_game(message: Message):
    bot_choice = random_stone_knots_paper()
    await message.answer(text=f'Твой выбор - {message.text}\n'
                              f'Выбор оппонента - {bot_choice}\n'
                              f'{result_random(message.text, bot_choice)}')
    await message.answer(text='Сыграем еще раз?',
                         reply_markup=yes_no_kb)
