# PROBLEM 1 SOLUTION: Plot a Circle
# Course: Intensive Foundation of Computer Science using Python
# Equation: x² + y² = 1

"""
SOLUTION: Plot a circle centered at (0,0) with radius 1

This solution demonstrates:
- Parametric equations for a circle
- Using np.linspace() for smooth curves
- Importance of plt.axis('equal')
- Proper plot formatting and labeling
"""

import matplotlib.pyplot as plt
import numpy as np

def problem1():
    """
    Plot a circle centered at (0,0) with radius 1
    Equation: x² + y² = 1
    
    Method: Parametric equations
    - x = cos(θ)
    - y = sin(θ)
    where θ ranges from 0 to 2π
    """
    
    print("="*70)
    print("PROBLEM 1: Circle Plot")
    print("="*70)
    
    # Step 1: Create angles from 0 to 2π (0 to 360 degrees)
    # Using 100 points for a smooth circle
    theta = np.linspace(0, 2*np.pi, 100)
    print(f"✓ Created {len(theta)} points from 0 to 2π")
    
    # Step 2: Calculate x and y coordinates using parametric equations
    x = np.cos(theta)
    y = np.sin(theta)
    print(f"✓ Calculated x and y coordinates using parametric equations")
    
    # Step 3: Verify the equation x² + y² = 1
    verification = x**2 + y**2
    print(f"✓ Verification: x² + y² = {np.mean(verification):.10f} (should be 1.0)")
    
    # Step 4: Create the plot
    plt.figure(figsize=(8, 8))
    
    # Plot the circle
    plt.plot(x, y, 'b-', linewidth=2, label='x² + y² = 1')
    
    # Mark the center point
    plt.plot(0, 0, 'ro', markersize=10, label='Center (0, 0)')
    
    # Draw a radius line from center to edge (to the right)
    plt.plot([0, 1], [0, 0], 'r--', linewidth=2, label='Radius = 1')
    
    # Add coordinate axes
    plt.axhline(y=0, color='k', linewidth=0.5)  # x-axis
    plt.axvline(x=0, color='k', linewidth=0.5)  # y-axis
    
    # Add grid for reference
    plt.grid(True, alpha=0.3)
    
    # CRITICAL: Set equal aspect ratio so circle looks circular (not elliptical)
    plt.axis('equal')
    
    # Add labels and title
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Problem 1: Circle with Equation x² + y² = 1', 
              fontsize=14, fontweight='bold')
    
    # Add legend
    plt.legend(fontsize=10)
    
    # Set viewing window
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    
    # Display the plot
    print("✓ Displaying plot...")
    plt.show()
    
    print("="*70)
    print("PROBLEM 1 COMPLETE")
    print("="*70)

# Run the solution
if __name__ == "__main__":
    problem1()
    
    # Print additional information
    print("\nKEY CONCEPTS:")
    print("- Parametric equations: x = cos(θ), y = sin(θ)")
    print("- theta from 0 to 2π creates a full circle")
    print("- plt.axis('equal') is CRITICAL for circular appearance")
    print("- More points = smoother circle (we used 100)")
    
    print("\nCOMMON MISTAKES TO AVOID:")
    print("- Forgetting plt.axis('equal') → circle looks elliptical")
    print("- Using too few points (< 30) → polygon instead of circle")
    print("- Using degrees instead of radians")
    print("- Not including plt.show() at the end")
