import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

tips= sns.load_dataset('tips')

sns.violinplot(data=tips, x='day', y='total_bill')
plt.title('Distribution of Bills by Day')
plt.show()