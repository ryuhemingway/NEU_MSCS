"""
Problem 2: Sleep Debt
Name: Ryu Hemingway
NU ID: 003163519

# I confirm that AI code completion tools were disabled while writing this program.

A "sleep debt" represents the difference between a person's desirable and 
actual amount of sleep. Write a program that prompts the user to enter how 
many hours he or she slept each day over a period of 7 days. Using 8 hours 
per day as the desirable amount of sleep, determine his or her sleep debt by 
calculating the total hours of sleep they got over the seven-day period and 
subtracting that from the total hours of sleep he or she should have got. 
If the user does not have a sleep debt, display a message expressing your jealousy.
"""

def get_sleep_hours(num_days):
    """  
    Prompt the user to enter hours slept for each day.
    """
    total_sleep = 0.0
    for day in range(1, num_days + 1):
        # Take input and convert to float:
        hours = float(input(f"Enter hours slept for day {day}: "))
        total_sleep += hours
    return total_sleep

def calculate_sleep_debt(true_hours, target_hours):
    """
    Calculate the difference between true sleep and target sleep hours.
    
    Parameters:
        true_hours (float): Total hours actually slept
        target_hours (float): Total hours that should have been slept
    
    Returns:
        float: The sleep debt accumulated thus far
    """
    return target_hours - true_hours

def display_sleep_debt_results(sleep_debt):
    """
    Display the sleep debt results with appropriate message.
    """
    if sleep_debt > 0:
        print(f"You have a sleep debt of {sleep_debt:.1f} hours. Time for a nap!")
    else:
        # If debt is 0 or negative, they are well-rested
        print("Woah buddy, you actually got enough sleep? I'm incredibly jealous! Must be nice. Good for you.... *sideeye*")


def main():
    """
    Main function to run the sleep debt calculator.
    """
    # Constants
    TARGET_HOURS_PER_DAY = 8
    NUM_DAYS = 7
    
    # 1. Get total true sleep hours from user
    true_total = get_sleep_hours(NUM_DAYS)
    
    # 2. Calculate total target sleep hours
    target_total = TARGET_HOURS_PER_DAY * NUM_DAYS
    
    # 3. Calculate sleep debt
    debt = calculate_sleep_debt(true_total, target_total)
    
    # 4. Display results
    display_sleep_debt_results(debt)

# Run the program
main()
