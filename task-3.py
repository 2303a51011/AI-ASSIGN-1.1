# write a python code program to calulate factorial using a user-defined function
# use meaningful variable names and add inline comments 
def calculate_factorial(num):
    # This function calculates the factorial of a given number
    if num < 0:
        return None
    
    result = 1
    for i in range(2, num + 1):
        result *= i  # Multiply result by each number up to num
    return result


# Main execution block
num = int(input("Enter a number: "))
factorial_result = calculate_factorial(num)
if factorial_result is None:
    print(f"Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial_result}.")