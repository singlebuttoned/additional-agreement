
import os

from .get_docx import read_docx
# from get_doc import read_doc
async def get_file_by_id(path_data, folder_id):
    """Асинхронно ищет DOCX или DOC файл по ID (имени папки)."""
    folder_path = os.path.join(path_data, folder_id)

    if not os.path.isdir(folder_path):
        raise ValueError(f"Папка с ID '{folder_id}' не найдена.")

    # Ищем первый DOCX или DOC файл в указанной папке
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.docx'):
            text = await read_docx(file_path)
            return file_name, text
        # elif file_name.endswith('.doc'):
        #     text = await read_doc(file_path)
        #     return file_name, text


    raise FileNotFoundError(f"В папке '{folder_id}' не найдено файлов с расширением .docx или .doc.")


async def print_docs(id_doc):
    PATH_DATA = 'C:\\Users\\al\\Desktop\\data'
    folder_id = id_doc  # Замените на нужный вам ID (имя папки)

    try:
        file_name, text = await get_file_by_id(PATH_DATA, folder_id)
        print(f'Файл: {file_name}\nТекст:\n{text}\n')
    except (ValueError, FileNotFoundError) as e:
        print(e)


