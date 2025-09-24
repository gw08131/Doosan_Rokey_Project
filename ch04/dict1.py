""""
리스트 = [값1, 값2, 값3]            #[0],[1],[2] <-인덱스 번호로 구분
변수명 = {키1:값1, 키2:값2, 키3:값3}         #키1번 값, 키2번 값, 키3번 값 <-키로 구분
"""

my_dict0 = {}                    #빈 dictionary
my_dict0 = {0:1, 1:-2, 2:3.14}  
print(my_dict0)

print('-------------------')

my_dict1 = {'이름':'앨리스', '나이':10, '시력':[1.0,1.2]}      #키(인덱스) 번호를 원하는데로 설정 가능
print(my_dict1['이름'])                              #앨리스
print(my_dict1['나이'])
print(my_dict1['시력'])

print('   수정-------------------')
#dic은 수정 가능!
my_dict1['나이'] = 11
my_dict1['시력'] = [0.9, 1.0]
print(my_dict1)

print("   추가-------------------")
my_dict1['직업'] = '서버'
my_dict1['키'] = '110cm'
print(my_dict1)


print("   가져오기-------------------")
print(my_dict1.get('직업'))
print(my_dict1['나이'])


print("items 출력-------------------")
dic_items = my_dict1.items()
print(dic_items)                #Tuple로 데이터들 가져옴 -> dict_items([('이름', '앨리스'), ('나이', 11), ('시력', [0.9, 1.0]), ('직업', '서버'), ('키', '110cm')])
print(type(dic_items))          #<class 'dict_items'> 띠용??

for item in dic_items:              #반복문으로도 가능!
    print(item)


print("keys출력-------------------") 
#print(my_dict1.keys())
for key in my_dict1.keys():
    print(key)

print("values-------------------") 
#print(my_dict1.values())
for value in my_dict1.values():
    print(value)


