# Multitreading in python
# Multithreading in Python allows you to run multiple threads (smaller units of a process) concurrently within a single process. 
# This can be useful for performing tasks that are I/O-bound (e.g., reading/writing files, making network requests) or for improving the responsiveness of a program by allowing it to perform multiple tasks at the same time.
import threading
import time

# Define a function that will be run in a separate thread
def fun(duration):
    print(f"Function taking time to execute...{duration} seconds")
    time.sleep(duration)  # Simulate a long-running task by sleeping for the specified duration
#Create a thread that will run the print_numbers function
time1 = time.perf_counter()  # Start the timer
fun(3)
fun(2)
fun(1)
time2 = time.perf_counter()  # End the timer
print(f"Time taken to execute the functions sequentially: {time2 - time1} seconds")

print("\nNow running the functions concurrently using threads...\n")
time1 = time.perf_counter()  # Start the timer
# Create threads for each function call
number_thread = threading.Thread(target=fun, args=(3,)) 
number_thread2 = threading.Thread(target=fun, args=(2,))
number_thread3 = threading.Thread(target=fun, args=(1,))
# Start the thread( this only starts the thread, it does not wait for the thread to finish)
number_thread.start()
number_thread2.start()
number_thread3.start()



time2 = time.perf_counter()  # End the timer
print(f"Time taken to execute the functions concurrently: {time2 - time1} seconds")

print("\n The actual time take to execute the functions concurrently will be approximately the time taken by the longest function, \n which is 3 seconds in this case, plus a small overhead for thread management.")
# Wait for all threads to finish (this will block the main thread until the threads complete)
number_thread.join()
number_thread2.join()
number_thread3.join()
time2 = time.perf_counter()  # End the timer after all threads have completed
print(f"Total time taken to execute the functions concurrently (including waiting for threads to finish): {time2 - time1} seconds")

# Now why use, let say you have to download multiple files from the internet, 
# if you do it sequentially, it will take a lot of time, but if you use multithreading, 
# you can download multiple files concurrently, which can significantly reduce the total time taken to download all the files.
# and all the files download at the same time, so the total time taken will be approximately the time taken by the longest download, rather than the sum of all download times.


# Ab ThreadPoolExecutor ko samjhate hain, jo ki concurrent.futures module ka part hai.
# ThreadPoolExecutor hame ek pool of threads create karne ki suvidha deta hai, jisme hum multiple tasks ko submit kar sakte hain aur wo threads un tasks ko concurrently execute karte hain.
# Iska matlab hai ki hum apne tasks ko easily manage kar sakte hain without manually creating and managing threads.
from concurrent.futures import ThreadPoolExecutor
# Define a function that will be run in a separate thread
def fun(duration):
    print(f"Function taking time to execute...{duration} seconds")
    time.sleep(duration)  # Simulate a long-running task by sleeping for the specified duration
    return f"Completed after {duration} seconds"
# Create a ThreadPoolExecutor with a specified number of worker threads
def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor for concurrent execution
       result = executor.submit(fun, 3)  # This will run fun(3) in a separate thread
       result2 = executor.submit(fun, 2)  # This will run fun(2) in a separate thread
       result3 = executor.submit(fun, 1)  # This will run fun(1) in a separate thread
        # Wait for the results and print them
       print(result.result())  # This will block until fun(3) is complete and then print the result
       print(result2.result())  # This will block until fun(2) is complete and then print the result
       print(result3.result())  # This will block until fun(1) is complete and then print the result
# Run the main function
if __name__ == "__main__":
    main()