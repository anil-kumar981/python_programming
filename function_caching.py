# Function caching example using functools.lru_cache
# The functools.lru_cache decorator is a built-in Python decorator that provides a simple way to
# cache the results of a function based on its input arguments. This can improve performance by avoiding redundant calculations for previously seen inputs.
from functools import lru_cache
import time
@lru_cache(maxsize=None)  # Cache results of the function with unlimited size
def fun(n):
    # Simulate a time-consuming computation
    time.sleep(2)  # Sleep for 2 seconds to simulate a long-running task
    return n * n  # Return the square of the input number
# Call the function with some input and measure the time taken
print(fun(4))  # This will take approximately 2 seconds to compute and return 16
print(fun(2))  # This will take approximately 2 seconds to compute and return 4
print(fun(4))  # This will return the cached result immediately, so it will be much faster and return 16 without the delay
print(fun(2))  # This will also return the cached result immediately, so it will be much faster and return 4 without the delay