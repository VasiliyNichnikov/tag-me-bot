import logging

from aiogram import executor

from app import dp


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
