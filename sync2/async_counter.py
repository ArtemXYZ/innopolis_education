import asyncio


class AsyncCounter:
    """
        Асинхронный счетчик.
    """

    def __init__(self):

        self.lock = asyncio.Lock()
        self.counter = 0


    async def lock_counter(self, increment):
        """
            Блокировщик асинхронного доступа к счетчику.
        """

        async with self.lock:
            self.counter += increment
            print(f'Срабатывание счетчика в режиме "lock" {self.counter} ')


    async def create_task(self, increment):
        """
            Создание задачи.
        """

        return asyncio.create_task(self.lock_counter(increment))

    async def add_tasks(self, numb_tasks: int = 10, increment: int = 5):
        """
            Запуск задач.
        """

        task_list = [self.create_task(increment) for _ in range(numb_tasks)]
        await asyncio.gather(*task_list)

async def main():
    counts = AsyncCounter()
    await counts.add_tasks()
    return print(f"Итоговое значение счетчика: {counts.counter}")


if __name__ == '__main__':
    asyncio.run(main())