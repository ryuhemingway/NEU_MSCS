# I confirm that AI code completion tools were disabled while writing this program.
# Name: Ryu Hemingway
# NU ID: 003163519

"""
Problem 4: Recursive List Sum

Design a function that accepts a list of numbers as an argument. The function should 
recursively calculate the sum of all the numbers in the list and return that value.
"""


def recursive_sum(numbers):
# create base case so no stack overflow
    if not numbers:
        return 0
    
# create recursion case to count down to base case and calculate the sum of the numbers
    return numbers[0] + recursive_sum(numbers[1:])

def main():
    """
    Main function to test the recursive_sum function
    """
    # Test case 1: list of positive integers
    test_list1 = [1, 2, 3, 4, 5]
    print(f"Test List 1: {test_list1}")
    print(f"Sum: {recursive_sum(test_list1)}")
    print(f"Expected: 15\n")
    
    # Test case 2: list with negative numbers
    test_list2 = [10, -5, 3, -2, 7]
    print(f"Test List 2: {test_list2}")
    print(f"Sum: {recursive_sum(test_list2)}")
    print(f"Expected: 13\n")
    
    # Test case 3: empty list
    test_list3 = []
    print(f"Test List 3: {test_list3}")
    print(f"Sum: {recursive_sum(test_list3)}")
    print(f"Expected: 0\n")
    
    # Test case 4: list with one element
    test_list4 = [42]
    print(f"Test List 4: {test_list4}")
    print(f"Sum: {recursive_sum(test_list4)}")
    print(f"Expected: 42\n")
    
    # Test case 5: list with floats
    test_list5 = [1.5, 2.3, 3.7, 4.5]
    print(f"Test List 5: {test_list5}")
    print(f"Sum: {recursive_sum(test_list5)}")
    print(f"Expected: 12.0\n")
    
    # User input test
    print("--- User Input Test ---")
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        user_list = [float(x) for x in user_input.split()]
        print(f"Your list: {user_list}")
        print(f"Sum: {recursive_sum(user_list)}")
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")


if __name__ == "__main__":
    main()
