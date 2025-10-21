# seaborn_basic.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로드
iris = sns.load_dataset("iris")
# print(iris)
# print(type(iris))           # <class 'pandas.core.frame.DataFrame'>

# 2. 기본 스타일 설정
sns.set_theme(style="whitegrid")

# 3. 그래프 표시
sns.scatterplot(data=iris,
                x="sepal_length",
                y="sepal_width",
                hue="species")


plt.title("Iris Dataset")
plt.show()