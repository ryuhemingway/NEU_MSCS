import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

tips = sns.load_dataset('tips')

sns.pairplot(tips, hue='time')
plt.show()