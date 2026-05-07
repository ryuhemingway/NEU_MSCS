# PROBLEM 3: Population Growth Simulation with While Loop
# Course: Intensive Foundation of Computer Science using Python
# Utilize: While loop + Conditionals + Lists + Subplots

"""
PROBLEM 3: Simulate population growth with conditions and plot the results

SCENARIO:
Simulate population growth for a city over time. Use a while loop to continue
until certain conditions are met. Store data in lists and visualize growth.

REQUIREMENTS:
1. Start with initial population of 1000
2. Use a while loop that continues until:
   - Population exceeds 10,000 OR
   - 50 years have passed
3. Each year:
   - If population < 5000: growth rate is 8%
   - If population >= 5000: growth rate is 5%
   - If year is divisible by 10: there's a special event (add 500 people)
4. Store year and population in separate lists
5. Create TWO subplots side by side:
   a. Left subplot: Line plot of population over time
   b. Right subplot: Bar chart showing growth for each decade
6. Add annotations for special events on the line plot
7. Print final population and years elapsed

HINTS:
- While loop: while population < 10000 and year < max_years:
- Check divisibility: if year % 10 == 0:
- Create subplots: fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
- Plot on specific subplot: ax1.plot(...) or ax2.bar(...)
- Annotations: ax1.annotate(text, xy=(x, y), ...)
- Keep track of special event years in a separate list

YOUR CODE BELOW:
"""

import matplotlib.pyplot as plt
import numpy as np

def problem3():
    """
    Simulate population growth with conditions
    """
    
   # YOUR CODE HERE
   # Step 1: Initialize variables
   # We begin with the parameters we need to start:
population = 1000
year = 0
max_years = 50

years_list = [0]     
pop_list = [1000]      
special_events = []
   
   # Step 2: While loop for simulation
   # We are asked for a while loop in the problem so we integrate it into our code
while population < 10000 and year < max_years:
   year += 1
   
   # Use a if/ifel,else to determine growth rate
   if population < 5000:
         growth_rate = 0.08
   else:
         growth_rate = 0.05
         
   # Apply standard growth
   population = population * (1 + growth_rate)

   if year % 10 == 0:
         population += 500
         special_events.append((year, population))
         
# Store values
years_list.append(year)
pop_list.append(population)

# --- Step 3: Setup the Figure ---
plt.figure(figsize=(16, 6))

   # --- Step 4: Left subplot - Line plot ---
plt.subplot(1, 2, 1) # (1 row, 2 columns, 1st position)
plt.plot(years_list, pop_list, color='tab:blue', linewidth=2, label='Population')
   
# Add annotations for special events (must be called while subplot 1 is active)
for event_year, event_pop in special_events:
      plt.annotate('Special Event!', 
                  xy=(event_year, event_pop), 
                  xytext=(event_year - 5, event_pop + 1000),
                  arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
   
plt.title('Population Growth Over Time')
plt.xlabel('Years')
plt.ylabel('Total Population')
plt.grid(True, alpha=0.3)

# --- Step 5: Right subplot - Bar chart ---
plt.subplot(1, 2, 2) # (1 row, 2 columns, 2nd position)

decades = [y for y in years_list if y % 10 == 0]
decade_pops = [pop_list[years_list.index(d)] for d in decades]

# we need to create and label our bar chart now
plt.bar([str(d) for d in decades], decade_pops, color='tab:orange', alpha=0.7)
plt.title('Population at Each Decade')
plt.xlabel('Year Mark')
plt.ylabel('Population')

# --- Step 6: Print summary and show plot ---
print(f"Simulation ended at Year {year}")
print(f"Final Population: {int(population)}")
plt.tight_layout() # Adjusts spacing between subplots
plt.show()

if __name__ == "__main__":
   problem3()
   print("Problem 3 complete!")