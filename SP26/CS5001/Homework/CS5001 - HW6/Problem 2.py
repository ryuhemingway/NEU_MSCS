# PROBLEM 2: Temperature Pattern Analysis with Nested Loops
# Course: Intensive Foundation of Computer Science using Python
# Utilize: Nested loops + Conditionals + Dictionaries + Line plot

"""
PROBLEM 2: Generate and plot temperature patterns for multiple cities

SCENARIO:
Create a line plot showing temperature patterns for 3 cities over 12 months.
Use nested loops to generate realistic temperature data and conditionals
to handle seasonal variations.

REQUIREMENTS:
1. Create a dictionary with 3 cities as keys
2. For each city, generate 12 monthly temperature values
3. Use nested loops: outer loop for cities, inner loop for months
4. Use conditionals to create realistic patterns:
   - Winter months (Dec, Jan, Feb): colder temperatures
   - Summer months (Jun, Jul, Aug): warmer temperatures
   - Spring/Fall months: moderate temperatures
5. Plot all three cities on the same graph with different colors
6. Add legend, labels, title, and grid
7. Mark the coldest and warmest month for each city

HINTS:
- Month indices: 0=Jan, 1=Feb, ..., 11=Dec
- Winter months: indices 0, 1, 11 (Dec, Jan, Feb)
- Summer months: indices 5, 6, 7 (Jun, Jul, Aug)
- Use different colors for each city
- Use plt.plot() with marker='o' for points
- Use min() and max() to find coldest/warmest temperatures
- Mark special points with '^' (triangle up) and 'v' (triangle down)

YOUR CODE BELOW:
"""

import matplotlib.pyplot as plt
import numpy as np

def problem2():
    """
    Generate and plot temperature patterns for multiple cities
    """
    
    # YOUR CODE HERE
    # Step 1: Create dictionary for cities and their temperatures
    # Made a dict for 3 cities
cities = {
    'San Jose': [52, 55, 58, 62, 68, 75, 80, 78, 74, 65, 57, 52],
    'Chicago':  [22, 26, 38, 50, 62, 72, 78, 76, 68, 55, 40, 27],
    'Miami':    [68, 70, 73, 77, 81, 85, 87, 88, 85, 80, 74, 69]
}
    
    # Step 2: Define month names
    # This was already provided
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

colors = ['blue', 'red', 'green']
city_names = list(cities.keys())

# Create our for loop 
for i in range(len(city_names)):
    city = city_names[i]
    temps = cities[city] 

    # Step 4: Create line plot for all cities using a similar format to the plot we made in class
    plt.plot(months, temps, marker='o', label=city)
        
    # Step 5: Mark min and max temperatures for each city. These are predefined.
    max_temp = max(temps)
    max_index = temps.index(max_temp)
    plt.plot(max_index, max_temp, marker='^', markersize=12)
    
    # Step 6: Add formatting (labels, title, legend, grid). Basically using the same format as our plots from class
    plt.title('Monthly Temperature Patterns by City')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°F)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Test the function
if __name__ == "__main__":
    problem2()
    print("Problem 2 complete!")
