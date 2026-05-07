import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

tips = sns.load_dataset('tips')

sns.boxplot(data=tips, x='day', y='total_bill')
plt.title('Total Bill by Day of Week')
plt.show()