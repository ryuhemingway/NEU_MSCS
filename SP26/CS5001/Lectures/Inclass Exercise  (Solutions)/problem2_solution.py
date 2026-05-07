# PROBLEM 2 SOLUTION: Plot a Square
# Course: Intensive Foundation of Computer Science using Python
# Center: (1, 1), Side Length: 2

"""
SOLUTION: Plot a square centered at (1,1) with side length 2

This solution demonstrates:
- Calculating corner coordinates from center and dimensions
- Closing polygons by repeating the first point
- Importance of plt.axis('equal') for squares
- Proper plot formatting
"""

import matplotlib.pyplot as plt
import numpy as np

def problem2():
    """
    Plot a square centered at (1,1) with side length 2
    
    Method: Calculate corner coordinates
    - Center: (1, 1)
    - Side length: 2
    - Half-side: 1
    - Corners: (cx±hs, cy±hs)
    """
    
    print("="*70)
    print("PROBLEM 2: Square Plot")
    print("="*70)
    
    # Step 1: Define square parameters
    center_x, center_y = 1, 1
    side_length = 2
    half_side = side_length / 2  # = 1
    
    print(f"Center: ({center_x}, {center_y})")
    print(f"Side length: {side_length}")
    print(f"Half-side: {half_side}")
    
    # Step 2: Calculate the four corners
    # Going counter-clockwise from bottom-left:
    x_corners = [
        center_x - half_side,  # Bottom-left x = 0
        center_x + half_side,  # Bottom-right x = 2
        center_x + half_side,  # Top-right x = 2
        center_x - half_side,  # Top-left x = 0
        center_x - half_side   # Back to bottom-left to close = 0
    ]
    
    y_corners = [
        center_y - half_side,  # Bottom-left y = 0
        center_y - half_side,  # Bottom-right y = 0
        center_y + half_side,  # Top-right y = 2
        center_y + half_side,  # Top-left y = 2
        center_y - half_side   # Back to bottom-left to close = 0
    ]
    
    print(f"\n✓ Corners calculated:")
    for i in range(4):
        print(f"  Corner {i+1}: ({x_corners[i]}, {y_corners[i]})")
    
    # Step 3: Create the plot
    plt.figure(figsize=(8, 8))
    
    # Plot the square
    plt.plot(x_corners, y_corners, 'g-', linewidth=2.5, label='Square (side=2)')
    
    # Mark the four corners with blue squares
    plt.plot(x_corners[:-1], y_corners[:-1], 'bs', markersize=8, label='Corners')
    
    # Mark the center with a red circle
    plt.plot(center_x, center_y, 'ro', markersize=10, label='Center (1, 1)')
    
    # Add coordinate axes
    plt.axhline(y=0, color='k', linewidth=0.5)  # x-axis
    plt.axvline(x=0, color='k', linewidth=0.5)  # y-axis
    
    # Add grid for reference
    plt.grid(True, alpha=0.3)
    
    # Add labels and title
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Problem 2: Square Centered at (1,1) with Side Length 2', 
              fontsize=14, fontweight='bold')
    
    # Add legend
    plt.legend(fontsize=10)
    
    # Set viewing window
    plt.xlim(-0.5, 2.5)
    plt.ylim(-0.5, 2.5)
    
    # CRITICAL: Set equal aspect ratio so square looks square (not rectangular)
    # Use 'box' adjustable to avoid warning
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Display the plot
    print("\n✓ Displaying plot...")
    plt.show()
    
    print("="*70)
    print("PROBLEM 2 COMPLETE")
    print("="*70)

# Run the solution
if __name__ == "__main__":
    problem2()
    
    print("\nKEY CONCEPTS:")
    print("- Corner calculation: center ± half_side for each coordinate")
    print("- Must repeat first point to close the square")
    print("- plt.gca().set_aspect('equal', adjustable='box') ensures square appears square")
    print("- Half-side = side_length / 2")
    
    print("\nCOMMON MISTAKES TO AVOID:")
    print("- Using side_length instead of half_side in calculations")
    print("- Not closing the square (only 4 points instead of 5)")
    print("- Forgetting to set aspect equal → rectangle instead of square")
    print("- Mixing up x and y coordinates")
