from dataclasses import dataclass
from functools import lru_cache

from environs import Env


@dataclass(frozen=True)
class Config:
    database_url: str
    secret_key: str
    debug: bool = False
    log_level: str = "INFO"


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        database_url=env.str("DATABASE_URL"),
        secret_key=env.str("SECRET_KEY"),
        debug=env.bool("DEBUG", default=False),
        log_level=env.str("LOG_LEVEL", default="INFO"),
    )


@lru_cache
def get_settings() -> Config:
    return load_config()
