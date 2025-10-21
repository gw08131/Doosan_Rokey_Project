# p1.py

food = ["김밥","만두", "양념치킨","족발","피자","쫄면","라면"]
ifood = iter(food)
print(type(food))               # <class 'list_iterator'>
for i_food in range(len(ifood)):
    print(i_food)

print(next(ifood))


