print("------------1번------------")
movie_rank = ['하얼빈', ' 무파사:라이온킹', '소방관']
print(movie_rank)

print("\n------------2번------------")
movie_rank.append('위키드')
print(movie_rank)

print("\n------------3번------------")
movie_rank.insert(3, '모아나2')
print(movie_rank)

print("\n------------4번------------")
movie_rank.remove('소방관')
print(movie_rank)

print("\n------------5번------------")
nums = [1, 2, 3, 4, 5]
sum = sum(nums[:])
print(sum)


print("\n------------6번------------")
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook[:]))



print("\n------------8번------------")
t = ('a', 'b', 'c')
list_t =list(t)
#print(type(list_t))
list_t[0] = 'A'
t = tuple(list_t)
print(t)

print("\n------------9번------------")
ice_cream = {'메로나': 1000, '폴라포': 1200, '빵빠레':1800}
print(ice_cream)

print("\n------------10번------------")
ice_cream['죠스바'] = 1200
ice_cream['월드콘'] = 1500
print(ice_cream)

print("\n------------11번------------")
ice_cream['메로나'] = 1300
print(ice_cream)