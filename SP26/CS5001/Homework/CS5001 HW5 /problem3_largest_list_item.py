# I confirm that AI code completion tools were disabled while writing this program.
# Name: Ryu Hemingway
# NU ID: 003163519

"""
Problem 3: Largest List Item

Design a function that accepts a list as an argument and returns the largest value 
in the list. The function should use recursion to find the largest item.
"""


def find_largest(lst):

# create a base case so we dont have stack overflow, then create recursive case. We already learned slicing so we will also slice the list to find the max num
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_largest(lst[1:]))

def main():
    """
    Main function to test the find_largest function
    """
    # Test case 1: list of integers
    test_list1 = [3, 7, 2, 9, 4, 1, 8]
    print(f"Test List 1: {test_list1}")
    print(f"Largest value: {find_largest(test_list1)}")
    
    # Test case 2: list with negative numbers
    test_list2 = [-5, -2, -10, -1, -7]
    print(f"\nTest List 2: {test_list2}")
    print(f"Largest value: {find_largest(test_list2)}")
    
    # Test case 3: list with one element
    test_list3 = [42]
    print(f"\nTest List 3: {test_list3}")
    print(f"Largest value: {find_largest(test_list3)}")
    
    # Test case 4: list with floats
    test_list4 = [3.5, 7.2, 2.1, 9.8, 4.3]
    print(f"\nTest List 4: {test_list4}")
    print(f"Largest value: {find_largest(test_list4)}")
    
    # User input test
    print("\n--- User Input Test ---")
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        user_list = [float(x) for x in user_input.split()]
        if user_list:
            print(f"Your list: {user_list}")
            print(f"Largest value: {find_largest(user_list)}")
        else:
            print("Empty list provided.")
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")


if __name__ == "__main__":
    main()
