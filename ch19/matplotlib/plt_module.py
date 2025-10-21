# plt_module.py

import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams["font.family"]= "Malgun Gothic"

# 선그래프
# x = [1,2,3,4]
# y = [10,20,25,30]
# plt.plot(x,y)
# plt.title("Line plot")
# plt.xlable("x-axis")
# plt.ylable("y-axis")
# plt.show()


#막대 그래프
# categories = ["A","B","C","D"]
# values = [3,7,8,5]
# plt.bar(categories,values,color='red')
# # plt.title("Bar Cart")
# plt.title("막대 그래프")
# plt.show()


# 히스토그램
# data = [1,2,2,3,3,3,4,4,4,4]
# # plt.hist(data,bins=4,color="skyblue",edgecolor="black")
# plt.hist(data,bins="auto",color="skyblue",edgecolor="black")
# plt.title("히스토그램")
# plt.show()


# 산점도 (Scatter Plot)
# x = [5,7,8,7,2,17,2,9,4,11]
# y=[99,86,87,88,100,86,103,87,94,78]
# plt.scatter(x,y,color="green")
# plt.title("Scatter Plot")
# plt.show()


# 파이 차트 (Pie Chart)
# sizes = [15, 30, 45, 10]
# labels = ["Group A", "Group B", "Group C", "Group D"]

# # %[flags][width][.precision][type]
# # %             서식지정자 시작
# # flags         정렬, 부호, 0채우기
# # width         최소출력너비(폭)
# # .precision    소수점이하자리수
# # type          형식문자

# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, counterclock=False)
# plt.title("Pie Chart")
# plt.show()

# 박스 플롯 (Box Plot)
# data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8]
# plt.boxplot(data)
# plt.title("Box Plot")
# plt.show()


# 커스터마이징
# x = [1,2,3,4]
# y = [10,20,30,40]

# # linestyle: '-' '--' ':' '-.' ...
# # marekr: '.' ',' 'o' '^' 'v' ...

# # plt.plot(x, y, color="red", linestyle="--", marker="o")
# plt.plot(x,y,"k^:")         # 줄여서 표현 가능 => black, ^모양, dotted line
# plt.title("Customized Line Plot")
# plt.show()


# x 축 범위와 눈금설정 
# x = [1,2,3,4]
# y = [10,20,30,40]
# plt.plot(x,y,"k^:") 
# plt.xlim(0,5)
# plt.ylim(0,40)
# plt.xticks(range(1,5))
# plt.yticks(range(0,41,10))
# plt.title("Customized Line Plot")
# plt.show()


# 법례 추가 및 위치 설정
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# x1 = [1, 2, 3, 4]
# y2 = [3, 5, 9, 7]
# plt.plot(x, y, label="Data 1")
# plt.plot(x1, y2, label="Data 2")
# plt.legend(loc="upper left")
# plt.savefig(r"C:\rokey\python\ch19\matplotlib\my_plot.png")
# plt.show()


# Subplot 활용 1
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
categories = ["A","B","C","D"]
values = [3,7,8,5]
data = [1,2,2,3,3,3,4,4,4]

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].bar(categories, values)
axs[1, 0].scatter(x, y)
axs[1, 1].hist(data)
plt.tight_layout()          # 여백을 타이트하게 만드는 용도 
plt.show()


# Subplot 활용 2
fig = plt.figure(figsize=(12,6))        # 도화지(Figure) 새성
ax1 = fig.add_subplot(2,2,1)            # 2행 2열로 화면 분할
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(x,y)
ax2.bar(categories, values)
ax3.scatter(x, y)
ax4.hist(data)
plt.tight_layout()
plt.show()