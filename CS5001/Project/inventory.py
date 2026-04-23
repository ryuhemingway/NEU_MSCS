
class Item:
    def __init__(self, name):
        # Only the name is needed since Inventory keys its dict by name
        self.name = name

class Inventory:
    # Set up the starting stock for every item on the menu
    def __init__(self):
        """
        type:dict
        Keys are item names (str), values are quantities (int)
        """
        # Dictionary mapping item name -> quantity on hand.
        # Keys match MenuItem.name exactly so that check_stock can find them
        self.stock = {
            # Drink
            "Latte": 5,
            "Espresso": 10,
            "Green Tea": 8,
            "Orange Juice": 0,
            # Food
            "Croissant": 4,
            "Bagel": 7,
            "Muffin": 5,
            "Sandwich": 2,
            # Dessert
            "Chocolate Croissant": 3,
            "Blueberry Muffin": 4,
            "Brownie": 0,
            "Cookie": 10,
            # Grab & Go
            "Chips": 12,
            "Popcorn": 0,
            "Granola Bar": 10,
            "Coke": 15,
            "Bottled Water": 20,
        }

    # Check if an item is available before letting the customer order it
    def check_stock(self, item):
        """
        returns: bool
        True if item.name has stock > 0, else False.
        """
        # .get(name, 0) returns 0 if the name isn't in the dict,
        # so an unknown item reads as "out of stock" instead of crashing
        return self.stock.get(item.name, 0) > 0

    # Reduce stock by 1 after a customer successfully adds an item to their cart
    def deduct_stock(self, item):
        """
        Only call after check_stock() returns True.
        returns: None
        Reduces stock for item.name by 1.
        """
        # Double-check stock here too so we never accidentally drop below 0
        if self.check_stock(item):
            self.stock[item.name] -= 1

    # Add more stock for a given item (used by staff restock mode)
    def restock(self, item_name: str, amount: int):
        """
        returns: None
        Increases stock for item_name by amount.
        """
        # Works for existing items (adds to current count) AND brand-new items
        # (starts from 0 via .get default), so it can introduce a new product too
        self.stock[item_name] = self.stock.get(item_name, 0) + amount

    # Print every item and its remaining quantity (used at end-of-session summary)
    def stock_report(self):
        """
        Prints all items and their current stock level.
        """
        # Loops over every key in self.stock and prints name + quantity
        for item_name in self.stock.keys():
            print(f"{item_name} remains: {self.stock[item_name]}")

# Guard so this test block only runs when you execute inventory.py directly.
# When main.py does `from inventory import Inventory`, this block is skipped.
if __name__ == "__main__":
    # Test block — exercises every method once
    inv1 = Inventory()
    sandwich = Item("Sandwich")       # fake item object with .name = "Sandwich"
    inv1.stock_report()                # show starting stock
    inv1.check_stock(sandwich)         # True — sandwich has stock 2
    inv1.deduct_stock(sandwich)        # stock drops to 1
    inv1.restock(sandwich.name, 10)    # stock jumps to 11
    inv1.check_stock(sandwich)         # still True
    inv1.stock_report()                # confirm the restock worked
    inv1.deduct_stock(sandwich)        # stock drops to 10
    inv1.stock_report()                # final state
