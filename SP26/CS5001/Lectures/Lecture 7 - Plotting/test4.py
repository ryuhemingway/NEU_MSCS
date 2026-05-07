import numpy as np
import matplotlib.pyplot as plt

# Drawing function sin(x) with different number of plots

# Try changing the N value to see what changes

N=10

x=np.linspace(0,2*np.pi, N)
y = np.sin(x)
plt.plot(x,y)
plt.show()
