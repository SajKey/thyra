from loguru import logger

from app.config import get_settings
from app.logger import setup_logging


def main() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)

    logger.info("thyra is running")
    logger.debug("debug mode: {}", settings.debug)


if __name__ == "__main__":
    main()
