# PROBLEM 4: Data Filtering and Visualization
# Course: Intensive Foundation of Computer Science using Python
# Utilize: Loops + Conditionals + List of dictionaries + Scatter plot

"""
PROBLEM 4: Filter and visualize data based on multiple conditions

SCENARIO:
You have sales data for a store. Filter the data based on conditions,
organize it in data structures, and create meaningful visualizations.

REQUIREMENTS:
1. Given lists of products, prices, and quantities sold
2. Create a list of dictionaries, where each dictionary represents a product
   with keys: 'name', 'price', 'quantity', 'revenue'
3. Use loops and conditionals to:
   - Calculate total revenue for each product (price × quantity)
   - Filter products into categories based on revenue:
     * High performers: revenue > $5000
     * Medium performers: $2000 <= revenue <= $5000
     * Low performers: revenue < $2000
4. Create a scatter plot where:
   - X-axis: Price
   - Y-axis: Quantity sold
   - Color: Different color for each performance category
   - Size: Proportional to revenue (revenue/10 works well)
5. Add product name labels next to each point
6. Add a legend explaining the color coding
7. Calculate and print summary statistics:
   - Total revenue across all products
   - Average revenue
   - Top performing product
   - Lowest performing product

HINTS:
- Create dictionary: {'name': products[i], 'price': prices[i], ...}
- Use .append() to add dictionaries to list
- Scatter for each category separately (different colors)
- Use plt.annotate() to add product labels
- Use max() with key parameter: max(list, key=lambda x: x['revenue'])

YOUR CODE BELOW:
"""

import matplotlib.pyplot as plt
import numpy as np

def problem4():
    """
    Filter and visualize sales data based on conditions
    """
    
    # Given data
    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam',
                'Headphones', 'Speaker', 'Microphone', 'Tablet', 'Phone']
    prices = [1200, 25, 75, 300, 80, 150, 200, 100, 500, 800]
    quantities = [5, 100, 50, 15, 40, 30, 20, 25, 12, 18]
    
    # YOUR CODE HERE
    # Step 1: Create list of dictionaries
    product_data = []
    for i in range(len(products)):
        revenue = prices[i] * quantities[i]
        product_dict = {
            'name': products[i],
            'price': prices[i],
            'quantity': quantities[i],
            'revenue': revenue
        }
        product_data.append(product_dict)
    
    # Step 2: Categorize products based on revenue
    # Create three empty lists: high_performers, medium_performers, low_performers
    # Loop through products_data and use conditionals to categorize
    high_performers = []
    medium_performers = []
    low_performers = []

    # use a for loop to loop through the preformers and append to the end of the list
    for item in product_data:
        if item['revenue'] > 5000:
            high_performers.append(item)
        elif 2000 <= item['revenue'] <= 5000:
            medium_performers.append(item)
        else:
            low_performers.append(item)
    
    # Step 3: Create scatter plot
    plt.figure(figsize=(12, 8))
    
    # Step 4-5: Plot each category with different colors
    # Loop through each category and plot
    categories = [
        (high_performers, 'green', 'High Performer (>$5k)'),
        (medium_performers, 'blue', 'Medium Performer ($2k-$5k)'),
        (low_performers, 'red', 'Low Performer (<$2k)')
    ]
    
    for cat_list, cat_color, cat_label in categories:
        if not cat_list: continue # Were going to skip if category is empty
        
        # Extract values for plotting
        x = [p['price'] for p in cat_list]
        y = [p['quantity'] for p in cat_list]
        sizes = [p['revenue'] / 10 for p in cat_list] 
        
        # Plot the category
        plt.scatter(x, y, s=sizes, color=cat_color, alpha=0.6, label=cat_label, edgecolors='black')
        
        # Add product name labels
        for p in cat_list:
            plt.annotate(p['name'], (p['price'], p['quantity']), 
                         textcoords="offset points", xytext=(0,10), ha='center')
    
    #Step 6: Add formatting similar to class plotting
    plt.title('Product Sales Performance Analysis', fontsize=14)
    plt.xlabel('Price ($)', fontsize=12)
    plt.ylabel('Quantity Sold', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Step 7: Calculate and print summary statistics
    all_revenues = [p['revenue'] for p in product_data]
    total_rev = sum(all_revenues)
    avg_rev = total_rev / len(product_data)
    
    top_prod = max(product_data, key=lambda x: x['revenue'])
    low_prod = min(product_data, key=lambda x: x['revenue'])
    
    print("-" * 30)
    print("SALES SUMMARY STATISTICS")
    print("-" * 30)
    print(f"Total Revenue:    ${total_rev:,.2f}")
    print(f"Average Revenue:  ${avg_rev:,.2f}")
    print(f"Top Performer:    {top_prod['name']} (${top_prod['revenue']})")
    print(f"Lowest Performer: {low_prod['name']} (${low_prod['revenue']})")
    print("-" * 30)
    
    # Step 8: Show the plot
    plt.show()

# Test your function
if __name__ == "__main__":
    problem4()
    print("Problem 4 complete!")
