import matplotlib.pyplot as plt
import numpy as np

N = 10000

x = np.linspace(0,2*np.pi,N)
y = np.sin(x)

plt.plot(x,y)

# change the fontsize and spacing of axes
plt.xticks(fontsize = 10)
plt.yticks(np.linspace(-1, 1, 5), fontsize = 10)

plt.figure(figsize=(20,10),dpi=50)
plt.plot([1,2,3], [1,4,9])

plt.show()