from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types.message import Message

from core.setup.bot import BOT
from modules.gpt_module.data.connect import gpt_connect
from modules.gpt_module.router import gpt_router


@gpt_router.message(Command("start"))
async def start_command(message: Message):
    await BOT.send_message(text="Привет\! Как я могу помочь вам сегодня\?", chat_id=message.chat.id,
                           parse_mode=ParseMode.MARKDOWN_V2)


@gpt_router.message()
async def gpt_answer(message: Message):
    text = ''
    waiting_message = await BOT.send_message(
        text="Решаю ваши вопросики...", chat_id=message.from_user.id
    )
    for i in range(4):
        text = await gpt_connect.get_answer(message.text)
        if text == '':
            continue
        else:
            break

    if text == '':
        text = "Сейчас не могу ничем помочь, попробуйте позже"

    await BOT.delete_message(chat_id=message.from_user.id, message_id=waiting_message.message_id)
    print(text)
    await BOT.send_message(text=text, chat_id=message.from_user.id, parse_mode=ParseMode.MARKDOWN_V2)
