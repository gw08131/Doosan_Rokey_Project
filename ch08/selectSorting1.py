# selectSorting1.py

ca = [21,10,11,15,13]
for i in range(0,len(ca),1):    #21~13까지 순차적으로 비교대상으로 설정
    mina=ca[i] 
    min_index = i
    #i 구간 이후에서 최솟값 찾기
    for sb in range(i,len(ca),1):   #ca list 값 5번 돌려서 비교해서 젤 작은 값 생성 + i대신 (i+1)이 mina랑 ca[i] 비교할 때 짜피 같은 데이터니까 불필요하긴함. 하지만 동작은 됨.
        if mina > ca[sb]:
            mina = ca[sb]    # 최솟값을 갱신
            min_index = sb   # 그 원소의 인덱스를 기록

    temp = ca[i]
    ca[i] = ca[min_index]
    ca[min_index] = temp

print(ca)


print("------------------")
ca = [21,10,11,15,13]
#1차 목표 ca = [10, 21, 11, 15, 13]
mina = ca[0]
min_index = 0
for sb in range(0,5,1):   
        if mina > ca[sb]:
            mina = ca[sb]    
            min_index = sb 
temp = ca[0]
ca[0] = ca[min_index]
ca[min_index] = temp
print(ca)       

#2차 목표 ca = [10,11,21,15,13]
mina = ca[1]
min_index = 1
for sb in range(1,5,1):   
        if mina > ca[sb]:
            mina = ca[sb]    
            min_index = sb 

temp = ca[1]
ca[1] = ca[min_index]
ca[min_index] = temp
print(ca)

#3차 목표 ca = [10,11,13,15,21]
mina = ca[2]
min_index = 2
for sb in range(2,5,1):   
        if mina > ca[sb]:
            mina = ca[sb]    
            min_index = sb 

temp = ca[2]
ca[2] = ca[min_index]
ca[min_index] = temp
print(ca)

#4차 목표 ca = [10,11,13,15,21]
mina = ca[3]
min_index = 3
for sb in range(3,5,1):   
        if mina > ca[sb]:
            mina = ca[sb]    
            min_index = sb 

temp = ca[3]
ca[3] = ca[min_index]
ca[min_index] = temp
print(ca)
