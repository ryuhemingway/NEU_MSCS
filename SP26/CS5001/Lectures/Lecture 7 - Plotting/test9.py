import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
scores = np.random.normal(75,10,100)

plt.hist(scores, bins=15)
plt.axvline(scores.min(), color='red', label='Lowest Score')
plt.axvline(scores.max(), color='green', label='Highest Score')
plt.axvline(scores.mean(), color='black', linestyle='--', label='Average')
plt.legend()
plt.show()