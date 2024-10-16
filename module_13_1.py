import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        await asyncio.sleep(5/power)
        print(f'Силач {name} поднял шар номер {i}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = start_strongman('Pasha', 3)
    task2 = start_strongman('Denis', 4)
    task3 = start_strongman('Appolon', 5)
