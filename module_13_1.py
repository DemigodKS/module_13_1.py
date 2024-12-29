import asyncio
from time import sleep


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i+1}')


    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1= asyncio.create_task(start_strongman('Nik', 3))
    task2 = asyncio.create_task(start_strongman('Veta', 5))
    task3 = asyncio.create_task(start_strongman('Kolya', 2))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())