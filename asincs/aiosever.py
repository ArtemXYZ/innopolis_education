import aiofiles
import asyncio
import csv
import json
import os


class Aiofiler:

    def __init__(self):
        pass

    @staticmethod
    async def aiowriter(
            filename: str,
            data: str | list | tuple,
            file_type: str = 'file',
            write_mode: str = 'w',
    ) -> None:
        """
            Универсальная функция для записи данных в файл.

            :param filename: Имя файла (включая путь).
            :param data: Данные для записи.
            :param file_type: Тип файла ('file', 'csv', 'json').
            :param write_mode: Режим записи ('w', 'a' и т.д.).
        """

        # Проверяем, существует ли директория, и создаем её, если нет
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        if file_type == 'csv':
            # Обработка CSV
            async with aiofiles.open(file=filename, mode=write_mode, newline='') as f:
                writer = csv.writer(f)
                if isinstance(data, list):
                    await writer.writerows(data)
                else:
                    raise ValueError("Для CSV данные должны быть списком списков.")

        elif file_type == 'json':
            # Обработка JSON
            async with aiofiles.open(filename, mode=write_mode) as f:
                await f.write(json.dumps(data, indent=4, ensure_ascii=False))

        elif file_type == 'file':
            # Обработка обычного текстового файла
            async with aiofiles.open(filename, mode=write_mode) as f:
                await f.write(str(data))

        else:
            raise ValueError(f"Неподдерживаемый тип файла: {file_type}")
