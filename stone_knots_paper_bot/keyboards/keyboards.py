from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создаем клавиатуру Давай/Не хочу
kb_builder = ReplyKeyboardBuilder()
play_btn = KeyboardButton(
    text='Давай!'
)
no_play_btn = KeyboardButton(
    text='Не хочу!'
)
kb_builder.row(play_btn, no_play_btn, width=2)
yes_no_kb: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

# Создаем клавиатуру камень/ножницы/бумага
game_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='камень🗿'),
                                         KeyboardButton(text='ножницы✂️'),
                                         KeyboardButton(text='бумага💶')]],
                              resize_keyboard=True,
                              one_time_keyboard=True,)
