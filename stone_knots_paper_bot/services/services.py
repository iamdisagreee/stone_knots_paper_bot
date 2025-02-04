import random

choices = {'камень🗿': 0,
           'ножницы✂️': 1,
           'бумага💶': 2}


def random_stone_knots_paper() -> str:
    return random.choice(['камень🗿', 'ножницы✂️', 'бумага💶'])


def _choice_winner(ind_user: int, ind_bot: int) -> str:
    if ind_user == ind_bot:
        return 'Ничья!'
    elif not ind_user and ind_bot == 1 or \
            ind_user == 1 and ind_bot == 2 or \
            ind_user == 2 and not ind_bot:
        return 'Ты победил!)'
    else:
        return 'Ты проиграл!('


def result_random(user_choice: str, bot_choice: str) -> str:
    ind_user = choices[user_choice]
    ind_bot = choices[bot_choice]

    return _choice_winner(ind_user, ind_bot)
