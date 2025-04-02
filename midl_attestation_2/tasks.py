"""
    Модель объекта Task.
"""

from src.services.tools import ServiceTols
from midl_attestation_2.commands import PingCommand


# ----------------------------------------------------------------------------------------------------------------------
class Task(ServiceTols):
    """
        Модель объекта "Задача". Реализует паттерн "команда".
    """

    def __init__(
            self,
            task_id: int = None,
            creation_time: float = None,
            title: str = None,
            command: PingCommand = None
    ) -> None:
        """
            Все атрибуты по умолчанию None, что бы можно было наследоваться без явной передачи аргументов.

            :arg task_id: id задачи.
            :arg creation_time: Время создания задачи.
            :arg title: Название задачи.
            :arg command: Переданная логика (паттерн команда).
        """

        super().__init__()
        self.task_id = task_id if self.validator(task_id, int | None) else ...
        self.creation_time = creation_time if self.validator(creation_time, float | None) else ...
        self.title = title if self.validator(title, str | None) else ...
        self.command = command if self.validator(command, PingCommand | None) else ...

    async def execute(self) -> None:
        """
            Метод обертка для универсальной реализации любой логики из переданного объекта (паттерн "команда").
            Выполняет переданную команду.
        """

        if self.command is not None:
            await self.command.execute(self.task_id, self.title)

    def __str__(self):
        # return ', '.join(f"{k}={v}" for k, v in vars(self).items())
        return str(vars(self))

    # Переопределяем после dataclass:
    def __repr__(self):
        return vars(self).__str__()
