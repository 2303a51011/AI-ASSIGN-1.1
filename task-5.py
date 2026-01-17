# generate an iterative factorial program using a loop include comments and meaningful variable names
def factorial_iterative(number):
    # Calculate factorial using an iterative approach (loop)
    result = 1
    for i in range(2, number + 1):
        result *= i  # Multiply result by each integer up to number
    return result
# generate a recursive factorial program
#ensure it returns the same output as the iterative version
def factorial_recursive(number):
    # Calculate factorial using a recursion approach
    if number < 0:
        return "Factorial is not defined for negative numbers"
    if number in (0, 1):
        return 1
    return number *factorial_recursive(number - 1)
# write main code to call both functions and display theirresults
number = int(input("Enter a number to calculate its factorial: "))
iterative_result = factorial_iterative(number)
recursive_result = factorial_recursive(number)
print(f"The factorial of {number} using iterative method is: {iterative_result}")
print(f"The factorial of {number} using recursive method is: {recursive_result}")

