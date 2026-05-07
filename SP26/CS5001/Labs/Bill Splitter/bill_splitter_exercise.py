"""
Bill Splitter Exercise - Foundations of Computer Science
Northeastern University Silicon Valley Campus

INSTRUCTIONS:
Complete the function below to calculate how much each person should pay
when splitting a restaurant bill among friends.

Your function should:
1. Add tax to the bill amount
2. Add tip (calculated on the after-tax amount)
3. Divide the total by the number of people
4. Round to 2 decimal places (cents)

DO NOT use AI assistants or code completion tools for this exercise.
This is designed to test your understanding of functions, parameters, and calculations.
"""


def split_bill(total_amount, num_people, tip_percent=18, tax_percent=8.5):
    """
    Calculate how much each person pays including tip and tax.
    
    Parameters:
    -----------
    total_amount : float
        Pre-tax bill amount in dollars
    num_people : int
        Number of people splitting the bill
    tip_percent : float, optional
        Tip percentage (default is 18%)
    tax_percent : float, optional
        Tax percentage (default is 8.5%)
    
    Returns:
    --------
    float
        Amount each person should pay, rounded to 2 decimal places
    
    Example:
    --------
    >>> split_bill(100, 4)
    31.63
    
    Explanation:
    - Subtotal: $100.00
    - Tax (8.5%): $8.50
    - After-tax total: $108.50
    - Tip (18% of $108.50): $19.53
    - Grand total: $128.03
    - Per person: $128.03 / 4 = $32.0075 → rounds to $32.01
    
    Note: The example above shows the calculation steps, but your actual
    implementation may have slight rounding differences depending on when
    you round. The test cases below show the expected outputs.
    """
    
    # TODO: Write your code here
    # Step 1: Calculate tax amount and add to total_amount
    tax = total_amount * (tax_percent / 100)
    total_with_tax = total_amount + tax

    # Step 2: Calculate tip amount (on the after-tax total) and add it
    tip = total_amount * (tip_percent / 100)
    total_with_tiptax = tip + total_with_tax

    # Step 3: Divide by num_people
    owed_per_person = total_with_tiptax / num_people

    # Step 4: Round to 2 decimal places
    return round(owed_per_person, 2)
  


# Test Cases
# ----------
# Run this file to test your function
# All test cases should print True if your function is working correctly

if __name__ == "__main__":
    print("Testing split_bill function...")
    print("-" * 50)
    
    # Test 1: Basic case with 4 people
    result1 = split_bill(100, 4)
    expected1 = 31.63
    print(f"Test 1: split_bill(100, 4)")
    print(f"  Expected: ${expected1}")
    print(f"  Got: ${result1}")
    print(f"  Pass: {abs(result1 - expected1) < 0.01}")
    print()
    
    # Test 2: 3 people with different subtotal
    result2 = split_bill(85.50, 3)
    expected2 = 36.06
    print(f"Test 2: split_bill(85.50, 3)")
    print(f"  Expected: ${expected2}")
    print(f"  Got: ${result2}")
    print(f"  Pass: {abs(result2 - expected2) < 0.01}")
    print()
    
    # Test 3: Custom tip percentage
    result3 = split_bill(120, 5, tip_percent=20)
    expected3 = 31.08
    print(f"Test 3: split_bill(120, 5, tip_percent=20)")
    print(f"  Expected: ${expected3}")
    print(f"  Got: ${result3}")
    print(f"  Pass: {abs(result3 - expected3) < 0.01}")
    print()
    
    # Test 4: Custom tip and tax percentages
    result4 = split_bill(50, 2, tip_percent=15, tax_percent=7)
    expected4 = 30.51
    print(f"Test 4: split_bill(50, 2, tip_percent=15, tax_percent=7)")
    print(f"  Expected: ${expected4}")
    print(f"  Got: ${result4}")
    print(f"  Pass: {abs(result4 - expected4) < 0.01}")
    print()
    
    # Test 5: Just 2 people, high bill
    result5 = split_bill(200, 2)
    expected5 = 128.03
    print(f"Test 5: split_bill(200, 2)")
    print(f"  Expected: ${expected5}")
    print(f"  Got: ${result5}")
    print(f"  Pass: {abs(result5 - expected5) < 0.01}")
    print()
    
    print("-" * 50)
    print("Testing complete!")
    print()
    print("EXTENSION CHALLENGES (Optional):")
    print("1. Add input validation: What if num_people is 0 or negative?")
    print("2. Create a version that returns a dictionary with breakdown:")
    print("   {'subtotal': X, 'tax': Y, 'tip': Z, 'total': W, 'per_person': P}")
    print("3. Add a discount_percent parameter for coupons/discounts")
    print("4. Handle the case where the bill doesn't split evenly")
    print("   (someone might need to pay 1 cent more)")
