import os

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class BotGetEnv(Bot):
    def __init__(self):
        """Переменные для подключения.

        - token_api: можно получить здесь: https://t.me/BotFather.
        - server_host: Привязывайте локальный хост только для предотвращения внешнего доступа.
        - server_port: Порт для входящего запроса от обратного прокси. Должен быть любой доступный порт.
        - webhook_url: Путь к маршруту веб-хука, по которому Telegram будет отправлять запросы.
        - webhook_path: часть пути, на который мы будем принимать запросы.
        - support_chat_id: группа, в которую будут отправлять запросы от пользователей.
        """
        self.TOKEN_API_TELEGRAM = self.get_str_from_env("TOKEN_API_TELEGRAM")
        self.SERVER_PORT = self.get_int_from_env("SERVER_PORT")
        self.WEBHOOK_URL = self.get_str_from_env("WEBHOOK_URL")
        self.WEBHOOK_PATH = self.get_str_from_env("WEBHOOK_PATH")
        self.PATH_DATA = self.get_str_from_env("PATH_DATA")
        self.DIFY_PUBLIC_CHAT_URL = self.get_str_from_env("DIFY_PUBLIC_CHAT_URL")

        super().__init__(self.TOKEN_API_TELEGRAM, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    def get_str_from_env(self, name: str) -> str:
        try:
            print(os.getenv(name))
            return str(os.getenv(name))
        except Exception as e:
            print(e)
            return ""

    def get_int_from_env(self, name: str) -> int:
        try:
            return int(os.getenv(name))
        except Exception as e:
            print(e)
            return 0


BOT = BotGetEnv()
