"""
    Модуль реализует работу объектов в соответствии с паттерном "КОМАНДА".
"""

import asyncio
from abc import ABC, abstractmethod
import random


# ----------------------------------------------------------------------------------------------------------------------
class CommandBase(ABC):
    """
        Абстрактная реализация команды (шаблон объекта логики).
    """

    @abstractmethod
    async def execute(self, task_id, title):
        pass


class PingCommand(CommandBase):
    """
        Конкретная реализация команды (имитирует работу задержкой).
    """

    def __init__(self):
        self.delay = random.randint(1, 10)
        pass

    async def execute(self, task_id, title):
        await asyncio.sleep(self.delay)
        print(f'В работе задача № {task_id}: {title}, ожидание: {self.delay} c.')



class CommandAggregator:
    """
        Интерфейс. Обработчик команд (посредник между бизнес логикой и интерфейсом).
    """

    def __init__(self, logic_command):
        # Принимаем (агрегируем) объект логики (ЛЮБУЮ команду)
        self.logic_command = logic_command

    def execute_command(self):
        self.logic_command.execute()  # Вызываем нужный метод

# # Объект логики:
# pg = PingCommand()
#
# # Объект обрабатывающий логику: # Объект срабатывающий по назначенной логике:
# cmd = CommandAggregator(pg)
#
# button.run_ping()
