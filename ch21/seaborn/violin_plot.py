# violin_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.set_theme(style="dark")

sns.violinplot(data=iris,
               x="species",
               y="sepal_length",
               inner="quart")

plt.title("Violin Plot Example")
plt.show()