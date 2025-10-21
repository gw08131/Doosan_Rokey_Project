# # Practice.py
# lst = [1,2,3,4,5,6]
# result = 0
# for i in range(len(lst)):
#     if lst[i] %2==0:
#         result = result+lst[i]
# print(result)

# # print("---------")
# # import re

# # text = input().strip()
# # matches = re.findall(r"[aeiou]",text,re.I)
# # result = len(matches)
# # print(result)


# print("---------")
# fruit = {"apple":3, "banana":2, "melon":5}
# lst = []
# for key in fruit:
#     print(key)
#     if fruit[key] >=3:
#         lst.append(key)
# print(lst)

# print("----------")
# try:
#     x = int('ten')
# except ValueError:
#     print("value error")
# else:
#     print("ok")
# finally:
#     print("done")

# print("----------")
# class Parent:
#     def sound(self):
#         print("부모가 소리냄!")

# class Dog(Parent):
#     def sound(self):
#         print("멍멍!")
#         # super().sound()  # 부모의 sound() 불러오기

# # d = Dog()
# # d.sound()
# p = Parent()
# p.sound()


print("------------")
g = {1:[2,3,4], 2:[1,5], 3:[1,6], 4:[1,6], 5:[2,6], 6:[3,4,5]}

def dfs(v, visited=[]):
    visited.append(v)
    print(visited)
    for node in g[v]:
        if node not in visited:
            dfs(node, visited)
    return visited

print(dfs(1))


print("------------")
import re
text = "Phone numbers: 010-1234-5678 and 010-2345-6789"
matches = re.findall(r"010-\d{4}-\d{4}",text)
print(matches)