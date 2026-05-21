# In C or C++, the switch statement is a control statement that allows a variable to be tested for equality against a list of values. Each value is called a case, and the variable being switched on is checked for each case.
# In Python, we have a similar construct called the (match) statement, which was introduced in Python 3.10. The match statement allows you to compare a value against a series of patterns and execute code based on which pattern matches.

# Here is an example of how to use the match statement in Python:
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
print(http_status(200))  # Output: "OK"

# In match there is no break statement like in C or C++. 
# Once a case is matched, the code block for that case is executed, 
# If no cases match, the code block under the default case (case _) is executed.