# Generator in python
# A generator in Python is a special type of iterator that allows you to,
# iterate over a sequence of values without storing the entire sequence in memory at once.
# A generator is defined using a function that contains one or more yield statements.
# When the generator function is called, it returns a generator object that can be iterated over. Each time the generator's __next__() method is called, the function executes until it reaches a yield statement, at which point it returns the yielded value and pauses its execution. The next time __next__() is called, the function resumes execution right after the yield statement.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Yield the current count value and pause execution
        count += 1  # Increment the count for the next iteration
# Create a generator object by calling the generator function
counter = count_up_to(5)
# Iterate over the generator object using a for loop
for number in counter:
    print(number)  # Output: 1, 2, 3, 4, 5

# Another example of a generator that generates an infinite sequence of Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a  # Yield the current Fibonacci number and pause execution
        a, b = b, a + b  # Update to the next Fibonacci numbers
# Create a generator object for the Fibonacci sequence
fib_gen = fibonacci()
# Iterate over the Fibonacci generator to get the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Using generators can be more memory efficient than using lists or other data structures to store large sequences of values, as they generate values on-the-fly and do not require storing the entire sequence in memory at once.