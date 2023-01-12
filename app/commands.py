from aiogram import types

from app import dp
from app.core.commands_utils import get_corrected_names
from app.core.config import get_config

config = get_config()


@dp.message_handler(commands=["all"])
async def send_welcome(message: types.Message):
    global config

    corrected_nicknames = get_corrected_names(config.tag.all)
    await message.answer(text=' '.join(corrected_nicknames))


@dp.message_handler(commands=["lol"])
async def send_welcome(message: types.Message):
    global config

    corrected_nicknames = get_corrected_names(config.tag.lol)
    await message.answer(text=' '.join(corrected_nicknames))



