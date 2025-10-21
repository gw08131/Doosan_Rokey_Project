# box_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset("iris")

sns.set_theme(style="dark")

sns.boxplot(data=iris,
            x="species",
            y="sepal_length")

plt.title("Box Plot Example")
plt.show()