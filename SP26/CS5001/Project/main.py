# main.py
# App Controller for Campus Café Ordering System
# Role D: Ryu, Shuran
# Course: CS 5001 / 5003 - Spring 2026

import random

from menu import MenuItem, MENU, display_menu, get_item
from order import Order
from inventory import Inventory

DAILY_SPECIAL_DISCOUNT = 0.20  # 20% off the daily special


def main():
    """
    Main application loop for the Campus Café ordering system.
    This coordinates MenuItem lookups, Order cart management, and Inventory stock tracking.
    """
    order = Order()
    inventory = Inventory()
    session_totals = []  # stores each checkout total as a float

    # Pick one random item from the menu as today's special (20% off).
    daily_special = random.choice(MENU)
    special_price = round(daily_special.price * (1 - DAILY_SPECIAL_DISCOUNT), 2)

    print("=" * 40)
    print("  Welcome to the NEU SV Campus Café!")
    print("=" * 40)
    print(f"  ⭐ Today's Special: {daily_special.name} "
          f"— 20% off! Now ${special_price:.2f} "
          f"(was ${daily_special.price:.2f})")
    print("=" * 40)

    def run_ordering_loop():
        """
        Inner ordering loop — shared by option 1 (View Menu) and option 2 (Order Item).
        Keeps prompting for item names and adding them to the cart until the user
        types 'b' to go back to the main menu.
        """
        first_prompt = True
        while True:
            if first_prompt:
                prompt = "Enter item name (or 'b' to go back): "
                first_prompt = False
            else:
                prompt = "What else would you like to order? (or 'b' to go back): "
            name = input(prompt).strip()

            if name.lower() == "b":
                break

            # Step 1: Look up the item
            item = get_item(MENU, name)

            # Step 2: Item not found — re-prompt in this inner loop
            if item is None:
                print("Item not found. Please enter the menu item exactly as shown.")
                continue

            # Step 3: Out of stock — re-prompt in this inner loop
            if not inventory.check_stock(item):
                print(f"Sorry, {item.name} is currently out of stock.")
                continue

            # Step 4: Add to cart (applying the daily-special discount if it matches)
            if item.name == daily_special.name:
                discounted = MenuItem(item.name, special_price, item.category)
                order.add_to_order(discounted)
                print(f"⭐ Daily special applied! {item.name} added at "
                      f"${special_price:.2f} (20% off).")
            else:
                order.add_to_order(item)
                print(f"{item.name} has been added to your cart!")

            # Step 5: Deduct from inventory (always the original item)
            inventory.deduct_stock(item)

    def print_session_summary():
        print("\n" + "=" * 40)
        print("        --- SESSION SUMMARY ---")
        print("=" * 40)
        print(f"  Orders completed: {len(session_totals)}")
        print(f"  Total revenue:    ${sum(session_totals):.2f}")

        if session_totals:
            print()
            for i, total in enumerate(session_totals, start=1):
                print(f"  Order {i}: ${total:.2f}")

        print("\n  Remaining Inventory:")
        inventory.stock_report()
        print("=" * 40)
        print("Goodbye! Thanks for visiting the Campus Café.")

    try:
      while True:
        # Display menu options
        print("\n--- What would you like to do? ---")
        print("[1] View Menu")
        print("[2] Order Item")
        print("[3] View Cart")
        print("[4] Checkout")
        print("[q] Quit")

        choice = input("Enter your choice: ").strip()

        # ------------------------------------------
        # Option 1: View the full menu, then drop straight into the ordering
        # loop so the user can start typing an item without pressing 2 first.
        # ------------------------------------------
        if choice == "1":
            display_menu(MENU)
            print(f"  ⭐ Daily Special: {daily_special.name} "
                  f"— 20% off! Now ${special_price:.2f}")
            run_ordering_loop()

        # ------------------------------------------
        # Option 2: Order an item
        # 5-step sequence:
        #   1. get_item() -> MenuItem or None
        #   2. Guard against None
        #   3. check_stock() -> True or False
        #   4. add_to_order() -> item goes in cart
        #   5. deduct_stock() -> stock decreases by 1
        # ------------------------------------------
        elif choice == "2":
            run_ordering_loop()

        # ------------------------------------------
        # Option 3: View current cart
        # ------------------------------------------
        elif choice == "3":
            order.display_order()

        # ------------------------------------------
        # Option 4: Checkout
        # Must save total before clearing the cart
        # ------------------------------------------
        elif choice == "4":
            # Checker — empty cart
            if not order.items:
                print("Your cart is empty. Add some items before checking out!")
                continue

            # Print the receipt
            print("\n" + "=" * 40)
            print("          --- RECEIPT ---")
            print("=" * 40)
            order.display_order()
            print("-" * 40)

            # Payment loop — this will accept partial payments until the balance is covered.
            total = order.get_total()
            remaining = total
            while remaining > 0.005:
                try:
                    payment = float(
                        input(f"Amount due: ${remaining:.2f}: $").strip()
                    )
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if payment <= 0:
                    print("Payment must be greater than zero.")
                    continue

                if payment + 0.005 < remaining:
                    # Too little — reprompt for the rest
                    remaining = round(remaining - payment, 2)
                    print(f"Received ${payment:.2f}. Remaining balance: ${remaining:.2f}")
                elif abs(payment - remaining) < 0.005:
                    # Exact payment
                    print("Payment accepted. Thank you!")
                    remaining = 0
                else:
                    # Overpayment — return change
                    change = round(payment - remaining, 2)
                    print(f"Payment accepted. Your change is ${change:.2f}. Thank you!")
                    remaining = 0

            print("=" * 40)

            # Save the total then clear the cart — customer can keep shopping
            # or press 'q' to see the session summary and quit.
            session_totals.append(total)
            order.clear_order()

        # ------------------------------------------
        # Quit: Show session summary and exit
        # ------------------------------------------
        elif choice.lower() == "q":
            print_session_summary()
            break

        # ------------------------------------------
        # Invalid input
        # ------------------------------------------
        else:
            print("Invalid option. Please enter 1, 2, 3, 4, or q.")
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or Ctrl+D at ANY prompt in the session — exit 
        print_session_summary()


if __name__ == "__main__":
    main()