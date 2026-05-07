# PLOTTING ASSIGNMENT
# Course: Intensive Foundation of Computer Science using Python
# Topic: Data Visualization with Matplotlib

"""
ASSIGNMENT INSTRUCTIONS:
========================

This assignment contains 4 problems that will test your understanding of:
- Basic plotting with matplotlib
- Parametric equations
- Random number generation and histograms
- 3D plotting

Each problem builds on concepts from the previous one. Complete all problems
and submit your Python file along with saved images of your plots.

DUE DATE: [Instructor will fill in]
TOTAL POINTS: 100 (25 points each problem)

SUBMISSION REQUIREMENTS:
- Submit this .py file with your solutions
- Create a folder named "plots" with all saved images
- Name your images: problem1.png, problem2.png, problem3.png, problem4.png
- Include comments explaining your approach
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# ==============================================================================
# PROBLEM 3: Dice Roll Histogram (25 points)
# ==============================================================================
print("\nPROBLEM 3: Dice Roll Histogram")
print("-"*70)

"""
PROBLEM 3 INSTRUCTIONS:
-----------------------
Generate a histogram that displays the outcomes and frequencies for the 
sum of two dice (each die has values 1-6).

REQUIREMENTS:
1. Simulate rolling two dice and adding their values
2. Start with 100 rolls, then show 1,000 rolls, then 10,000 rolls
3. Create 3 subplots (side by side or stacked) showing how the distribution
   changes with more rolls
4. The sum of two dice ranges from 2 to 12
5. Use appropriate bins (bins=11 for values 2-12)
6. Add vertical line showing the expected mean (which is 7)
7. Add titles, labels, and legends to each subplot
8. Save the plot as 'plots/problem3.png'

MATH BACKGROUND:
- Each die: 1-6 (uniform distribution)
- Sum of two dice: 2-12 (NOT uniform! 7 is most common)
- Expected value (mean): 7
- Most common sum: 7 (can be made 6 ways: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1)

GRADING:
- Correct simulation of dice rolls: 8 points
- Three subplots with different numbers of rolls: 8 points
- Proper histogram formatting (bins, labels): 5 points
- Mean line shown: 2 points
- Code quality and comments: 2 points

YOUR SOLUTION:
"""

def problem3():
    # YOUR CODE HERE
    # Hint for rolling dice:
    # die1 = np.random.randint(1, 7, n_rolls)  # Random integers from 1 to 6
    # die2 = np.random.randint(1, 7, n_rolls)
    # dice_sum = die1 + die2
    
    # Hint for subplots:
    # fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    # axes[0].hist(...)  # First subplot
    # axes[1].hist(...)  # Second subplot
    # axes[2].hist(...)  # Third subplot
    
    pass  # Remove this and write your code

# Uncomment to test your solution:
# problem3()

print("Status: TODO - Complete problem3() function")
