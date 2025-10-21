# facetgrid.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)

sns.set_theme(style="dark",palette="pastel")

g = sns.FacetGrid(tips,
                  col="sex",row="time",
                  height=3.5,
                  aspect=1.5)
g.map_dataframe(sns.scatterplot, x="total_bill", y = "tip")
g.set(xlim=(0,60),
      ylim=(0,12))
g.savefig(r"C:\rokey\python\ch21\seaborn\facet_plot.png")
g.tight_layout()

plt.show()