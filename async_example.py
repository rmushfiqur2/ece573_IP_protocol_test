# https://stackoverflow.com/questions/50757497/simplest-async-await-example-possible-in-python

# Read the link for here: In case 2, we added async to the normal function. However the event loop will run it without
# interruption. Why? Because we didn't say where the loop is allowed to interrupt your function to run another task.

# when you write async within a async function, the main program creates another thread for that portion
# async function needs to run multpile times, every time when it gets async, it opens a thread
# two ways of adding multiple tasks

# 1. event loop
import asyncio
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])), # sum is an async function and contains a task/ portion starting with async
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 2.
task = asyncio.create_task(sum("A", [1, 2]))
# However you can't wait for the task to finish in the main program
# you can create another async function for waiting
async def main():
    task = asyncio.create_task(sum("A", [1, 2]))
    await task
    return task.result()
