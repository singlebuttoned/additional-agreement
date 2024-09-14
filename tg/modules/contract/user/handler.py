from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types.message import Message
from aiogram import  F
from modules.contract.data.connect import print_docs
from pyexpat.errors import messages

from core.setup.bot import BOT
# from modules.gpt_module.data.connect import gpt_connect
from modules.contract.router import contract_router


@contract_router.message(Command("start"))
async def start_command(message: Message):
    await BOT.send_message(text="Привет\! Как я могу помочь вам сегодня\?", chat_id=message.chat.id,
                           parse_mode=ParseMode.MARKDOWN_V2)


@contract_router.message(F.text.isdigit())
async def contract_command(message: Message):
    print(message.text)
    await print_docs(str(message.text))
    text = "Получил доку"
    await BOT.send_message(text=text, chat_id=message.chat.id,
                           parse_mode=ParseMode.MARKDOWN_V2)
