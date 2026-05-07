# PROBLEM 1: Plot a Circle
# Course: Intensive Foundation of Computer Science using Python
# Points: 25

"""
ASSIGNMENT: Plot a circle centered at the point (0, 0) with a radius of 1
where the equation of this circle is given by x² + y² = 1

REQUIREMENTS:
1. Use parametric equations: x = cos(θ), y = sin(θ)
2. Create at least 100 points for a smooth circle
3. Mark the center point with a different color/marker
4. Draw at least one radius line from center to the circle edge
5. Use plt.axis('equal') to ensure the circle looks circular (not elliptical)
6. Add appropriate labels for x and y axes
7. Add a descriptive title
8. Include a legend
9. Add a grid for reference
10. Display the plot with plt.show()

HINTS:
- Use np.linspace(0, 2*np.pi, 100) to create angles from 0 to 2π
- Remember: 2π radians = 360 degrees = full circle
- x = np.cos(theta), y = np.sin(theta)
- Without plt.axis('equal'), your circle will look like an ellipse!

YOUR CODE BELOW:
"""

import matplotlib.pyplot as plt
import numpy as np

def problem1():
    """
    Plot a circle centered at (0,0) with radius 1
    Equation: x² + y² = 1
    """
    
    # YOUR CODE HERE
    # Step 1: Create theta values from 0 to 2π
    
    
    # Step 2: Calculate x and y coordinates
    
    
    # Step 3: Create the plot
    
    
    # Step 4: Mark the center point
    
    
    # Step 5: Draw a radius line
    
    
    # Step 6: Add axes lines
    
    
    # Step 7: Add grid
    
    
    # Step 8: IMPORTANT - Set equal aspect ratio
    
    
    # Step 9: Add labels and title
    
    
    # Step 10: Add legend
    
    
    # Step 11: Display the plot
    plt.show()

# Test your function
if __name__ == "__main__":
    problem1()
    print("Problem 1 complete!")
