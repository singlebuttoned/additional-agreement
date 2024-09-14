from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

user_commands = [
    BotCommand(command="start", description="Запустить бота"),
]


async def update_commands(bot: Bot):
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())
