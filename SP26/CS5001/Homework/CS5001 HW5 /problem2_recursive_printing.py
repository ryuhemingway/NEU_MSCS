# I confirm that AI code completion tools were disabled while writing this program.
# Name: Ryu Hemingway
# NU ID: 003163519

"""
Problem 2: Recursive Printing

Design a recursive function that accepts an integer argument, n, and prints every 
second number from n down to a minimum of 0. Assume that n is always a 
positive integer.
"""


def recursive_print(n):

# begin with base case so we dont get stack overflow
    if n < 0:
        return
    
    print(n)

# apply recursive step so we dont get recursive error
    recursive_print(n-2)

def main():
    """
    Main function to test the recursive print function
    """
    
    # Get user input
    print("\n--- User Input Test ---")
    try:
        num = int(input("Enter a positive integer: "))
        if num >= 0:
            print(f"\nPrinting every second number from {num} down to 0:")
            recursive_print(num)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
