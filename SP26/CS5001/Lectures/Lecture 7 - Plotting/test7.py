import matplotlib.pyplot as plt

#example: programming languages popularity
Cities= ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Pheonix']
Population = [8.4,3.85,2.65,2.3,1.65]

plt.bar(Cities, Population, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.title('Population by City')
plt.xlabel('Cities')
plt.ylabel('Population Size in Millions')
plt.show()