
subject = ['국어', '수학', '영어', '국사']
subject.remove('영어')
print(subject)

print("--------------")
clovers = ['클로버1', '클로버2', '클로버3']
#print(clovers[1])
#del clovers[1]
#print(clovers[1])          #데이터가 인덱스 앞번호로 하나씩 당겨짐

print("--------------")
"""del clovers[1,2]"""
del clovers[1:3]            #del 리스트명[시작인덱스(start): 끝인덱스-1(end)]
print(clovers)