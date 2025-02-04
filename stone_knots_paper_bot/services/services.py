import random
from stone_knots_paper_bot.database.database import db

choices = {'камень🗿': 0,
           'ножницы✂️': 1,
           'бумага💶': 2}


def random_stone_knots_paper() -> str:
    return random.choice(['камень🗿', 'ножницы✂️', 'бумага💶'])


def _choice_winner(id_user: int, ind_user: int, ind_bot: int) -> str:
    _is_user_in_database(id_user)
    if ind_user == ind_bot:
        db[id_user][2] += 1
        return 'Ничья!'
    elif not ind_user and ind_bot == 1 or \
            ind_user == 1 and ind_bot == 2 or \
            ind_user == 2 and not ind_bot:
        db[id_user][0] += 1
        return 'Ты победил!)'
    else:
        db[id_user][1] += 1
        return 'Ты проиграл!('


def result_random(id_user, user_choice: str, bot_choice: str) -> str:
    ind_user = choices[user_choice]
    ind_bot = choices[bot_choice]

    return _choice_winner(id_user, ind_user, ind_bot)


def get_result(id_user):
    _is_user_in_database(id_user)
    return db[id_user]


def _is_user_in_database(id_user):
    if db.get(id_user) is None:
        db[id_user] = [0, 0, 0]
