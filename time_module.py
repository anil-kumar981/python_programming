# Time Module in python
# The time module in Python provides various functions to work with time-related tasks.
import time
# Get the current time in seconds since the epoch (January 1, 1970)
current_time = time.time()
print(f"Current time in seconds since the epoch: {current_time}")

# Now check a function that takes some time to execute, and we can measure how long it takes using the time module.
def long_running_function():
    print("Starting a long-running function...")
    time.sleep(2)  # Simulating a long-running task by sleeping for 2 seconds
    print("Finished the long-running function.")
# Measure the time taken to execute the long-running function
start_time = time.time()  # Record the start time
long_running_function()  # Call the long-running function
end_time = time.time()  # Record the end time   
elapsed_time = end_time - start_time  # Calculate the elapsed time
print(f"Time taken to execute the long-running function: {elapsed_time} seconds")