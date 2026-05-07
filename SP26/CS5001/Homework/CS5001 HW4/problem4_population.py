"""
Problem 4: Population
Name: Ryu Hemingway
NU ID: 003163519

# I confirm that AI code completion tools were disabled while writing this program.

Write a program that predicts the approximate size of a population of organisms. 
The application should prompt the user to enter the starting number of organisms, 
the average daily population increase (as a percentage), and the number of days 
the organisms will be left to multiply.

Example:
    Starting number of organisms: 2 
    Average daily increase: 30% 
    Number of days to multiply: 10

The program should display a table showing the population for each day.
"""

def get_population_inputs():
# prompt user for 3 inputs
    start_size = float(input("Starting number of organisms"))
    avg_increase = float(input("Average daily increase %"))
    days_to_grow = int(input("Number of days to grow: "))

    # Conv percentage to decial value
    growth_rate = avg_increase/ 100
    return start_size, growth_rate, days_to_grow

def calculate_next_day_population(current_pop, daily_rate):
    return current_pop * (1 + daily_rate)

def show_growth_table(start_pop, rate, total_days):
    print("\nDay\t\tPopulation")
    print("--------------------------")
    
    # Begin with the initial population on Day 1
    current_pop = start_pop
    
    for day in range(1, total_days + 1):
        # Show the current state before calculating the next day
        print(f"{day}\t\t{current_pop:.2f}")
        
        # Update the current_pop for the next iteration of the loop
        current_pop = calculate_next_day_population(current_pop, rate)

def main():
    """
    Main function to run the population growth predictor.
    """
    # get all 3 inputs from the function we made initially
    start, growth, days = get_population_inputs()
    
    # provide values to the table
    show_growth_table(start, growth, days)


# Run the program
main()
