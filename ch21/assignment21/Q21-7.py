# Q21-7.py

#7. seaborn을 사용하여 tips 데이터셋의 요일(day) 별
# 전체금액(total_bill)의 박스플롯을 그려보세요. 
# (seaborn.boxplot()을 사용하세요.)

import seaborn 
import matplotlib.pyplot as plt

tips = seaborn.load_dataset("tips")

seaborn.set_theme(style="dark")

seaborn.boxplot(data=tips,
                x="day",
                y="total_bill")
plt.title("Total Bills per Day")
plt.show()