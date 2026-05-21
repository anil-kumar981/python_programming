# Recursion in  Python
# Recursion is a programming technique where a function calls itself in order to solve a problem.
# A recursive function typically has two main components: a base case that stops the recursion, 
# and a recursive case that breaks the problem into smaller subproblems and calls itself to solve those subproblems.

# Here is an example of a recursive function that calculates the factorial of a number:
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# Debugging a recursive function can be challenging, but it can be helpful to add print statements to see the flow of the function calls. For example:
def factorial(n):
    print(f"Calculating factorial({n})")  # Debugging statement
    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        result = n * factorial(n - 1)
        print(f"Result of factorial({n}): {result}")  # Debugging statement
        return result
print(factorial(5))  # Output: 120