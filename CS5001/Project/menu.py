# menu.py
# Name: Lanqi Yi, Hanwen Wang
# NU ID: 003118670, 003182499
# Course: CS 5001 / 5003 -Spring 2026

from __future__ import annotations

class MenuItem:

    def __init__(self, name: str, price: float, category: str):
        """
        The attributes of a menu item, including validation for name and price.

        Parameters:
            name (str): item name, e.g. "Latte" 
            price (float): the price in dollars, e.g. 4.50 
            category (str): item category, e.g. "Drink" or "Food"
        """
        
        if not name or not name.strip():
            raise ValueError("Menu item name cannot be empty.")
        if price < 0:
            raise ValueError("Menu item price cannot be negative.")
        
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        """Return a formatted string, e.g. Latte (Drink) - $4.50"""
        return f"{self.name} ({self.category}) - ${self.price:.2f}"
    
MENU = [
    # Drink
    MenuItem("Latte", 4.50, "Drink"),
    MenuItem("Espresso", 3.00, "Drink"),
    MenuItem("Green Tea", 3.50, "Drink"),
    MenuItem("Orange Juice", 4.00, "Drink"),

    # Food
    MenuItem("Croissant", 3.25, "Food"),
    MenuItem("Bagel", 2.75, "Food"),
    MenuItem("Muffin", 2.50, "Food"),
    MenuItem("Sandwich", 6.50, "Food"),
    
    # Dessert
    # ALTERED FROM ORIGINAL: renamed "Croissant" -> "Chocolate Croissant" and
    # "Muffin" -> "Blueberry Muffin" below.
    # Why: the original MENU had duplicate names across categories ("Croissant"
    # in both Food and Dessert, "Muffin" in both Food and Dessert). That broke
    # two things:
    #   1. get_item() returns the FIRST name match, so the Dessert versions
    #      were unreachable — you could never order them.
    #   2. Inventory is keyed by name alone, so both versions would have
    #      shared a single stock count.
    # Unique names make every menu item addressable and independently tracked.
    MenuItem("Chocolate Croissant", 3.50, "Dessert"),
    MenuItem("Blueberry Muffin",    3.25, "Dessert"),
    MenuItem("Brownie",             3.00, "Dessert"),
    MenuItem("Cookie",              2.50, "Dessert"),

    # Grab & Go
    MenuItem("Chips",        2.00, "Grab & Go"),
    MenuItem("Popcorn",      2.50, "Grab & Go"),
    MenuItem("Granola Bar",  2.00, "Grab & Go"),
    MenuItem("Coke",         2.00, "Grab & Go"),
    MenuItem("Bottled Water", 1.50, "Grab & Go"),
]

def display_menu(menu: list[MenuItem]) -> None:
    """
    Prints all items grouped by category with prices.
    Arguments:
    menu (list of MenuItem): The list of menu items to display.
    Returns:
    None
    """
    # initialze an empty dictionary to store items by category
    category = {} 
    for item in menu: 
        """""
        iterate through each item in the menu
        if the category is not already a key in the dictionary, add it with an empty list
        if the category is already a key, append the item to the list of items for that category
        """
        if item.category not in category: 
            category[item.category] = []
        category[item.category].append(item)
   
    # print the menu header
    print("=" * 40)
    print("   ☕ NEU SILICON VALLEY CAFÉ MENU ☕")
    print("=" * 40)

    # Print items by category
    for key in sorted(category.keys()):
        print(f"\n---{key}---")
        for item in category[key]:
            # Set the total width to 30. The remaining part will be filled with dots. 
            # Default alignment is left. The price is formatted to 2 decimal places.
            print(f"  {item.name:.<30}${item.price:.2f}")

    print("\n" + "=" * 40) # the menu footer

def get_item(menu: list[MenuItem], name: str) -> MenuItem | None:
    """
    Searches the MENU list and returns the matching item, or None if not found.
    Arguments:  
    menu (list of MenuItem): The list of menu items to search through.
    name (str): The name of the item to search for.
    Returns:
    MenuItem | None: The matching menu item, or None if not found.
    """
    clean_name = name.strip() # remove the whitlespace from the input name
    # remove any non-alphanumeric characters from the input name and store the remaining characters in a list
    characters = []
    for ch in clean_name:
        if ch.isalpha() or ch.isspace():
            characters.append(ch)   
    # join the characters in the list to form a cleaned name string        
    final_name = ''.join(characters) 
    
    for item in menu:
        if item.name.lower() == final_name.lower():
            return item
    return None

if __name__ == "__main__":
    # Display the whole menu
    display_menu(MENU)
    
    # Search for the item named "Latte" and print the result
    result = get_item(MENU, "Latte")
    if result:
        print(f"Found: {result}")
    else:
        print("This item was not found on the menu.")
        
     # ----------- Test Block ---------------------------------------------
    print()
    print(">>> TEST 1: get_item() —  test case sensitivity: 'latte(Latte)'")
    result = get_item(MENU, "latte")
    if result:
        print(f"Found: {result}")
    else:
        print("This item was not found on the menu.")
    print()
    print(">>> TEST 2: get_item() — test whitespace handling: '  Bagel  '")
    result = get_item(MENU, "  Bagel  ")
    if result:
        print(f"Found: {result}")
    else:
        print("This item was not found on the menu.")

    print()
    print(">>> TEST 3: get_item() — item not on menu: 'Hahaha'")
    result = get_item(MENU, "Hahaha")
    if result:
        print(f"Found: {result}")
    else:
        print("This item was not found on the menu.")

    print()
    print(">>> TEST 3: get_item() — item not on menu: '3$Bagel'")
    result = get_item(MENU, "3$Bagel")
    if result:
        print(f"Found: {result}")
    else:
        print("This item was not found on the menu.")


    print()
    print(">>> TEST 4: __str__ output")
    sample = MenuItem("Latte", 4.50, "Drink")
    print(f"{sample}")

    print()
    print(">>> TEST 5: Invalid input — negative price")
    try:
        bad_item = MenuItem("Test Drink", -1.00, "Drink")
    except ValueError as e:
        print(f"Caught error: {e}")

    print()
    print(">>> TEST 6: Invalid input — empty name")
    try:
        bad_item = MenuItem("", 5.00, "Food")
    except ValueError as e:
        print(f"Caught error: {e}")
    
    print()
    print("All tests complete.")

