"""
    pass
"""

import asyncio
from asyncio import Semaphore

from asincs.aiosever import Aiofiler
from asincs.asinc_parser import Parser


# ======================================================================================================================
class RunAioPars:
    """
        pass
    """

    def __init__(self, semaphore_limit):

        self.parser = Parser()
        self.filer = Aiofiler()
        self.file_name = r'./ids.txt'
        self.tasks_list = []
        # Ограничиваем количество одновременных запросов:
        self.semaphore = asyncio.Semaphore(semaphore_limit)
        self.address = 'Samara'

    async def set_semaphore_for_task(self, coro):
        """
            Создаем задачи с учетом семафора.
            :param _semaphore:
            :param coro:
            :return:
        """

        async with self.semaphore:

            # Выполняем основную задачу (парсинг или загрузку данных).
            result = await coro

            # Сразу после выполнения основной задачи (до)записываем результат в файл:
            await self.filer.aiowriter(self.file_name, data=result, write_mode='a')

            return result

    async def set_tasks(self):
        """
            Основная функция.
            :return:
        """

        # Создаем задачи:
        self.tasks_list.append(self.set_semaphore_for_task(self.parser.sitemap.get_categories_id_from_sitemap()))
        self.tasks_list.append(self.set_semaphore_for_task(self.parser.winter.decode_address(self.address)))


        return await asyncio.gather(*self.tasks_list)

async def runer():
    """
        Обертываем в асинхронную функцию основную логику для запуска корутины.
    """
    runner = RunAioPars(2)
    return await runner.set_tasks()

if __name__ == '__main__':
    results = asyncio.run(runer())
    print("Результаты выполнения задач:", results)