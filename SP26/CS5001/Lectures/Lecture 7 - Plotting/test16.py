import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

tips = sns.load_dataset('tips')

correlation = tips.corr(numeric_only=True)

sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()