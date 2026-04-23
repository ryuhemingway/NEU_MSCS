#Name: Jiayi Wang, Jessie Lin
#NUID: 003186999, 003950726
class Order:
    """
    Manages the customer's shopping cart for one café session.
    Holds a list of MenuItem objects and computes the running total.
    """

    def __init__(self):
        """Start with an empty cart (self.items = [])."""
        # Initialize a list to hold MenuItem objects as the customer adds them
        self.items = []

    def add_to_order(self, item):
        """
        Append a MenuItem to the cart.

        Parameters:
            item (MenuItem): the item the customer wants to order.
        Returns:
            None
        """
        # Whenever customers order, put the dish in the cart
        self.items.append(item)

    def get_total(self):
        """
        Sum the prices of every item currently in the cart.

        Returns:
            float: total price, 0.0 for an empty cart.
        """
        # Get the present price of items in cart
        total = 0.0
        for i in self.items:
            total = total + i.price
        return total

    def display_order(self):
        """
        Print each item (name, category, price) and the running total.
        Prints a friendly message if the cart is empty.

        Returns:
            None
        """
        # Display every item with a clear layout, then the total at the bottom
        if len(self.items) > 0:
            for i in self.items:
                print(f"{i.name} ({i.category}): {i.price:.2f}" )
            print(f"Total: {self.get_total():.2f}")
        else:
            print("Your cart is empty, please add items to cart:")

    def clear_order(self):
        """
        Empty the cart. Called after a successful checkout.

        Returns:
            None
        """
        # Reset the cart back to an empty list
        self.items = []

#Make sure test block doesn't run when my teamate imports this file
if __name__ == "__main__":

    #Test block
    class FakeItem:
        def __init__(self, name, price, category):
            self.name = name
            self.price = price
            self.category = category

    latte = FakeItem("Latte", 4.50, "Drink")
    muffin = FakeItem("Muffin", 3.00, "Dessert")
    noodles = FakeItem("Noodles", 12.00, "Food")

    #Test cases
    print("---- Test function one by one ----")
    my_order = Order()
    my_order.add_to_order(latte)
    my_order.add_to_order(muffin)
    my_order.add_to_order(noodles)
    print(my_order.items)
    print(my_order.get_total())
    my_order.display_order()

    #Special case
    print("---- Test if we clear cart, what will happen ----")
    my_order.clear_order()
    my_order.display_order()
    print(my_order.get_total())