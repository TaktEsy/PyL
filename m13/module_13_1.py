import asyncio

async def start_strongman(name, power):
    ball = 1
    print(f"Силач {name} начал соревнования")
    while ball <= 5:
        await asyncio.sleep(1/power)
        print(f"Силач {name} поднял {ball} шар.'")
        if ball == 5:

            print(f"Силач {name}  закончил соревы!'")
        ball += 1

async def start_tournament():
    t1 = asyncio.create_task(start_strongman("Вася", 3))
    t2 = asyncio.create_task(start_strongman("Петя", 4))
    t3 = asyncio.create_task(start_strongman("Гоша", 5))
    await t1
    await t2
    await t3

asyncio.run(start_tournament())