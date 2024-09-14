import asyncio
from docx import Document

async def read_doc(file_path):
    """Асинхронно читает текст из DOC файла."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, lambda: extract_text_from_doc(file_path))


def extract_text_from_doc(file_path):
      doc = Document(file_path)

      # Получаем текст из файла
      text = []
      for paragraph in doc.paragraphs:
          text.append(paragraph.text)

      # Выводим содержимое файла
      print('\n'.join(text))
