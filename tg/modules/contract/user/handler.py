from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types.message import Message
from core.setup.bot import BOT
from modules.contract.router import contract_router


@contract_router.message(Command("start"))
async def start_command(message: Message):
    await BOT.send_message(text="Привет\! Как я могу помочь вам сегодня\?", chat_id=message.chat.id,
                           parse_mode=ParseMode.MARKDOWN_V2)


