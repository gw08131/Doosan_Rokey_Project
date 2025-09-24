# selectSorting6.py

def fselsort(cb):
    for i in range(0,len(cb),1):    #21~13까지 순차적으로 비교대상으로 설정
        mina=cb[i] 
        min_index = i
        for sb in range(i+1,len(cb),1):   #cb list 값 5번 돌려서 비교해서 젤 작은 값 생성 + i대신 (i+1)이 mina랑 ca[i] 비교할 때 짜피 같은 데이터니까 불필요하긴함. 하지만 동작은 됨.
            if mina > cb[sb]:
                mina = cb[sb]    # 최솟값을 갱신
                min_index = sb   # 그 원소의 인덱스를 기록

        temp = cb[i]
        cb[i] = cb[min_index]
        cb[min_index] = temp
    return cb

ca = [21,10,11,15,13]
cc = [10,4,8,2,6,1,9,5,7,3]
#sorted_list = fselsort(ca)
#print(sorted_list)
print(fselsort(ca))
print(fselsort(cc))