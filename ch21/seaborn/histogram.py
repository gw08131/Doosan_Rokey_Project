# histogram.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.set_theme(style="darkgrid")

sns.histplot(data=iris,
             x="sepal_length",
             hue="species",
             kde=True)
plt.title("Hitogram Example")
plt.show()