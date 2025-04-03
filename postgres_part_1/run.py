"""
    Интерфейс взаимодействия с пользователем.
"""
from postgres_part_1.interface import PostgeInterface

interface = PostgeInterface()


def runner():

    interface.power()


if __name__ == '__main__':
    runner()
