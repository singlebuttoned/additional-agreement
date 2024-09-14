from docx import Document

import asyncio
import os

async def read_docx(file_path):
    """Асинхронно читает текст из DOCX файла."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, lambda: extract_text_from_docx(file_path))


def extract_text_from_docx(file_path):
    """Извлекает текст из DOCX файла."""
    doc = Document(file_path)
    return '\n'.join(paragraph.text for paragraph in doc.paragraphs)





