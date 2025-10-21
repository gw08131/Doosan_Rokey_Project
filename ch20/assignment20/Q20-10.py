# Q20-10.py

# 10. 다음 그룹 A 데이터에 대한 기본 통계를 
# 계산하는 프로그램을 작성하시오.
# 그룹 A: [80, 85, 90, 75, 95]

from scipy.stats import describe

A = [80, 85, 90, 75, 95]
print(describe(A))