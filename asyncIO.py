# Asynchronous I/O in python(asyncio)
# Asynchronous programming in Python is a programming paradigm that allows you to write code that can perform multiple tasks concurrently without blocking the execution of other tasks. 
# The asyncio module in Python provides a framework for writing asynchronous code using coroutines, which are special functions that can pause and resume their execution.
import asyncio
# Define an asynchronous function (coroutine) that simulates a long-running task
async def long_running_task(task_name, duration):
    print(f"Starting {task_name}...")
    await asyncio.sleep(duration)  # Simulate a long-running task by sleeping for the specified duration
    print(f"Finished {task_name}.")

async def short_task(task_name):
    print(f"Starting {task_name}...")
    await asyncio.sleep(0.1)  # Simulate a short task by sleeping for 0.5 seconds
    print(f"Finished {task_name}.")
# Define the main function that will run multiple asynchronous tasks concurrently
async def main():
    # Create a list of tasks to run concurrently
    tasks = [
        long_running_task("Task 1", 2),  # This task will take 2 seconds to complete
        long_running_task("Task 2", 3),  # This task will take 3 seconds to complete
        long_running_task("Task 3", 1),   # This task will take 1 second to complete
        short_task("Short Task 1"), 
        short_task("Short Task 2")
    ]

    # Run the tasks concurrently and wait for them to finish
    await asyncio.gather(*tasks)
# Run the main function using asyncio
asyncio.run(main())