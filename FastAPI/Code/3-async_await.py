# def sum(a, b):
#     return a + b

# print(sum(5, 7))

import asyncio

async def sum(a, b):
    return a + b

async def print_sum(a, b):
    result = await sum(a, b)
    print(f'Resultado é igual a {result}')

# res = sum(100, 589)
# print(res)

# Event Loop
# evt_loop = asyncio.new_event_loop()
# result = evt_loop.run_until_complete(res)
# print(result)

evt_loop = asyncio.new_event_loop()
result = evt_loop.run_until_complete(print_sum(20, 40))

