from dataclasses import dataclass
from environs import Env


@dataclass
class Tgbot:
    token: str


@dataclass
class Config:
    tgBot: Tgbot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tgBot=Tgbot(token=env('BOT_TOKEN')))

