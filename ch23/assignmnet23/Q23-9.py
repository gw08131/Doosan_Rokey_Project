import matplotlib.pyplot as plt

# 한글 폰트 설정 (Malgun Gothic)
plt.rcParams['font.family'] = 'Malgun Gothic'

fruits = ["사과", "바나나", "오렌지", "포도", "딸기"]
sales = [50, 80, 40, 70, 90]

# 막대 그래프
plt.bar(fruits, sales, color='skyblue')

plt.title("과일별 판매량")
plt.xlabel("과일")
plt.ylabel("판매량(개)")
plt.tight_layout()
plt.show()
