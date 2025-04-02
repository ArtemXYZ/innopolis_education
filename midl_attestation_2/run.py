"""
    Интерфейс взаимодействия с пользователем.
"""

import asyncio
from midl_attestation_2.interface import ApplicationInterface

interface = ApplicationInterface()


async def runner():

    await interface.power()


if __name__ == '__main__':
    asyncio.run(runner())
