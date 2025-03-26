# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking user input
number = int(input("Enter a number to calculate its factorial: "))

# Calling the factorial function and displaying the result
result = factorial(number)
print(f"The factorial of {number} is {result}")

