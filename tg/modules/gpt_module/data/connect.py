import os
import urllib.parse

import aiohttp
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class GPTConnect:
    def __init__(self):
        """Например: https://Домен/api/gpt/request="""
        self.WEB_PATH_API_GPT = self.get_str_from_env("WEB_PATH_API_GPT")

    def get_str_from_env(self, name: str) -> str:
        try:
            print(os.getenv(name))
            return str(os.getenv(name))
        except Exception as e:
            print(e)
            return ""

    async def get_answer(self, request: str):
        request = urllib.parse.quote(request).replace("/", "\\")

        url = f"{self.WEB_PATH_API_GPT}{request}"  # Укажите URL вашего FastAPI endpoint

        async with aiohttp.ClientSession() as session, session.get(url) as response:
            if response.status == 200:
                data = await response.json()  # Парсим JSON ответ
                print(data)
                data = escape_characters(data)
                print(data)
                return data
            else:
                return str(response.status)


def escape_characters(text):

    special_characters = ['_', '[', ']', '(', ')', '<', '>', '*', '#', '+', '-', '\\', '=', '|', '{', '}', '.', '!']

    escaped_text = ''
    for char in text:
        if char in special_characters:
            escaped_text += '\\' + char
        else:
            escaped_text += char
    escaped_text = escaped_text.replace('\\*\\*', '\\**').replace('\\*', '')
    escaped_text = escaped_text.replace('*', '***')
    escaped_text = escaped_text.replace('\\|\\|', '||')
    escaped_text = escaped_text.replace('\\_\\_', '_')
    escaped_text = escaped_text.replace('~~', '~')
    escaped_text = escaped_text.replace('\\`\\`\\`', '```')
    print(escaped_text)
    return escaped_text


gpt_connect = GPTConnect()
