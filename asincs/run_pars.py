"""
    pass
"""

import asyncio
from asincs.asinc_parser import Parser

# ======================================================================================================================
async def runer():
    """
        Основная функция.
        :return:
    """

    tasks_list = []

    parser = Parser()

    # Ограничиваем количество одновременных запросов до 2
    semaphore = asyncio.Semaphore(2)

    # Создаем задачи с учетом семафора
    async with semaphore:
        tasks_list.append(await parser.sitemap)
        # tasks_list.append(await parser.sitemap)


    # Запускаем все задачи параллельно
    result_list = await asyncio.gather(*tasks_list)


    # Сохраняем результаты:
    for result in tasks_list:
        print(result)




if __name__ == '__main__':
    asyncio.run(runer())