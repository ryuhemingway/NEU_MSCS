# PROBLEM 2: Plot a Square
# Course: Intensive Foundation of Computer Science using Python
# Points: 25

"""
ASSIGNMENT: Plot a square centered at the point (1, 1) with a side length of 2

REQUIREMENTS:
1. Calculate the four corner points of the square
   - Center: (1, 1)
   - Side length: 2
   - Half-side length: 1
   - Corners should be at: (0, 0), (2, 0), (2, 2), (0, 2)
2. Plot the square by connecting all corners
3. Close the square (connect back to the first corner)
4. Mark the center point with a different color/marker
5. Use plt.gca().set_aspect('equal', adjustable='box') to ensure the square looks square
6. Add labels, title, and grid
7. Display the plot with plt.show()

HINTS:
- If center is (cx, cy) and half-side is hs:
  * Bottom-left corner: (cx - hs, cy - hs)
  * Bottom-right corner: (cx + hs, cy - hs)
  * Top-right corner: (cx + hs, cy + hs)
  * Top-left corner: (cx - hs, cy + hs)
- To close the square, repeat the first point at the end
- Use lists for x and y coordinates: x = [x1, x2, x3, x4, x1]
"""

import matplotlib.pyplot as plt
import numpy as np

def problem2():
    """
    Plot a square centered at (1,1) with side length 2
    """
    
    # YOUR CODE HERE
    # Step 1: Define center and side length
    
    
    # Step 2: Calculate half-side
    
    
    # Step 3: Calculate the four corners (and repeat first to close)
    
    
    # Step 4: Create the plot
    
    
    # Step 5: Plot the square
    
    
    # Step 6: Mark corners
    
    
    # Step 7: Mark center
    
    
    # Step 8: Add axes lines
    
    
    # Step 9: Add grid
    
    
    # Step 10: IMPORTANT - Set equal aspect ratio
    
    
    # Step 11: Add labels and title
    
    
    # Step 12: Add legend
    
    
    # Step 13: Display the plot
    plt.show()

# Test your function
if __name__ == "__main__":
    problem2()
    print("Problem 2 complete!")
