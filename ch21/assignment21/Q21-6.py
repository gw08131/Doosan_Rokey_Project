# Q21-6.py

# 6. seaborn을 사용하여 임의의 데이터를 생성하고 히스토그램을 그려보세요.
# numpy를 사용하여 평균이 50, 표준편차가 10인 정규 분포 데이터를 1000개 생성하세요.
# seaborn.histplot()을 사용하여 히스토그램을 시각화하세요.

import seaborn 
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(50,100,1000)
#print(data)

seaborn.histplot(data,
              kde=True)

plt.title("Normal Distribution (mean=50, std=10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()