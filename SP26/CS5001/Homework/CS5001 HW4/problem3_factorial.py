"""
Problem 3: Calculating the Factorial of a Number
Name: Ryu Hemingway
NU ID: 003163519

# I confirm that AI code completion tools were disabled while writing this program.

In mathematics, the notation n! represents the factorial of the nonnegative 
integer n. The factorial of n is the product of all the nonnegative integers 
from 1 to n. For example:
    7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5,040
    4! = 1 x 2 x 3 x 4 = 24

Write a program that lets the user enter a nonnegative integer then uses a 
loop to calculate the factorial of that number. Display the factorial.
"""

def get_nonnegative_integer():
    user_input = int(input("Please enter a non-negative integer"))
    return user_input
    

def calculate_factorial(n):
# similar to what we did in class, calculate the factorial of a non-negative integer using the range func
    result = 1

    for i in range(1, n+1):
        result = result * i

    return result

def show_factorial_result(original_number, factorial_value):
    # display the result to the user showing their original number and the facotial value
    print(f"The factorial of {original_number} is {factorial_value}")

def main():
    """
    Main function to run the factorial calculator.
    """
    num = get_nonnegative_integer()

    answer = calculate_factorial(num)

    show_factorial_result(num, answer)

# Run the program
main()