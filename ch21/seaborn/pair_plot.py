# pair_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.set_theme(style="white")

sns.pairplot(iris,
             hue = "species")

plt.show()