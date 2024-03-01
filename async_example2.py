import asyncio
import time

async def my_async_function(v):
    # Your asynchronous code here
    abc = 2 + v
    await asyncio.sleep(1) # asyncio creates a new process (wait on another thread)
    return abc

async def sleep():
    print(f'Time: {time.time()}')
    await asyncio.sleep(1)


loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(my_async_function(10)),
    loop.create_task(my_async_function(50)),
]
done, pending = loop.run_until_complete(asyncio.wait(tasks))
#loop.close() # IMPORTANT: if you close event loop later tasks will not run

for future in done:
    value = future.result() #may raise an exception if coroutine failed
    print(value)
    # do something with value

# calling from another anync function (not convenient)
async def main():
    abc = await my_async_function(30) # it does not create a thread here, it will when it finds the actual async task inside the called function
    #print(abc)
    return abc

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(main()),
]
done, pending = loop.run_until_complete(asyncio.wait(tasks))
for future in done:
    value = future.result() #may raise an exception if coroutine failed
    print(value)
loop.close()