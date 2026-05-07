import matplotlib.pyplot as plt
import seaborn as sns
import ssl
import certifi
"/Applications/Python 3.14/Install Certificates.command"

tips = sns.load_dataset('tips')

lunch_data = tips[tips['time'] == 'Lunch']
dinner_data = tips[tips['time'] == 'Dinner']

plt.scatter(lunch_data['total bill'], lunch_data['tip'], color='orange', label='Lunch, alpha=0.6')
plt.scatter(dinner_data['total bill'], lunch_data['tip'], color='blue', label='Dinner, alpha=0.6')

plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Tips vs Total Bill by Time')
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.title('Tips vs Total Bill')
plt.show()