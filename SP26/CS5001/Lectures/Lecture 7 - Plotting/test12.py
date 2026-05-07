import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4], [1,4,9,16], label='Quadratic Growth', marker='o')
plt.plot([1,2,3,4], [1,4,9,16], label='Linear Growth', marker='s')

plt.legend(loc='upper left')
plt.title('Growtj Comparison')
plt.xlabel('Time')
plt.ylabel('Value')

# Add annotation
plt.annotate('Inflection point', xy=(3,9), xytext=(2,12), arrowprops=dict(arrowstyle='->', color='red'))
plt.show()
