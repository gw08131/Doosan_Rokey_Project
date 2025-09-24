#find_max1.py

ca = [10,17,13,11]
max = ca[0]
if max < ca[1]:
    max = ca[1]
if max < ca[2]:
    max = ca[2]
if max < ca[3]:
    max = ca[3]
print(max)

print("-----------------------")
ca = [10,17,13,11]
max = ca[0]
for num in range(0,len(ca),1):
    if max < ca[num]:
        max = ca[num]
    num =+ 1
print(max)