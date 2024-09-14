import asyncio
import logging
import sys

from aiogram import Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from core.setup.bot import BOT
from core.setup.menu_command import update_commands
from core.setup.middleware import ThrottlingMiddleware, WaitingCallbackMiddleware
from modules.routers import modules_router


class DispatcherBot(Dispatcher):
    def __init__(self):
        super().__init__()

    def run_to_polling(self) -> None:
        self.register_modules()
        asyncio.run(self.polling_startup())

    async def polling_startup(self) -> None:
        await update_commands(BOT)
        await BOT.delete_webhook()
        await self.start_polling(BOT)

    def run_to_webhook(self) -> None:
        self.register_modules()
        self.startup.register(self.webhook_startup)
        app = web.Application()

        webhook_requests_handler = SimpleRequestHandler(
            dispatcher=self,
            bot=BOT,
        )

        webhook_requests_handler.register(app, path="/" + BOT.WEBHOOK_PATH)
        setup_application(app, self, bot=BOT)
        web.run_app(app, port=BOT.SERVER_PORT)

    @staticmethod
    async def webhook_startup() -> None:
        await update_commands(BOT)
        await BOT.set_webhook(f"{BOT.WEBHOOK_URL}/{BOT.WEBHOOK_PATH}")

    def register_modules(self):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        self.include_routers(modules_router)
        self.message.middleware.register(ThrottlingMiddleware())
        self.callback_query.middleware.register(WaitingCallbackMiddleware())
