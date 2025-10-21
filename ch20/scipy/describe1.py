# describe1.py

from scipy.stats import describe

data = [1,2,3,4,5,6,7]
stats = describe(data)
print(stats)

# 외도(skewness)는 분포의 비대칭 정도
# 첨도 (Kurtois)는 분포의 뽀족한 정도