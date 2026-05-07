import numpy as np
import matplotlib.pyplot as plt

#create 2x2 grid of plots
fig, axes = plt.subplots(2,2, figsize=(12,10))

#plot 1: Line plot
axes[0,0].plot([1,2,3,4], [1,4,9,16])
axes[0,0].set_title('Line Plot')

#plot 2: scatter plot
axes[0,1].scatter([1,2,3,4], [1,4,9,16], color='blue')
axes[0,0].set_title('Scatter Plot')

#plot 3: Bar chart
axes[1,0].bar(['A','B','C'], [3,7,5], color='red')
axes[1,0].set_title('Bar Chart')

#plot 4: Histogram
axes[1,1].hist(np.random.randn(100), bins=20)
axes[1,1].set_title('Histogram')

plt.tight_layout()
plt.show()