#find_max2.py

su = [5,4,7,10,6]
def fmax(a,b,c,d,e):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e 
    return max

print("최대값:",fmax(su[0],su[1],su[2],su[3],su[4]))


print("-----------------------")
su = [5,4,7,10,6]
def fmax(a,b,c,d,e):
    fu = [a,b,c,d,e]
    max = fu[0]
    for sfu in range (0,5,1):
        if max < fu[sfu]:
            max = fu[sfu]
    return max

max = fmax(su[0],su[1],su[2],su[3],su[4])       #이 max는 global 변수라서 지역변수 max랑은 다름
print("최대값:",max)


print('---------------------')
def fmax(a,b,c,d,e):
    fu = []
    fu.append(a)
    fu.append(b)
    fu.append(c)
    fu.append(d)
    fu.append(e)
    max = a
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su[0],su[1],su[2],su[3],su[4])       #이 max는 global 변수라서 지역변수 max랑은 다름
print("최대값:",max)


print('---------------------')
def fmax(fu):
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

su = [5,4,7,10,6]
print("최대값:",fmax(su))


print('---------------------')
def fmax(fu):
    max = fu[0]
    for i in range(1,len(fu),1):
        if max < fu[i]:
            max = fu[i]
    return max

su = [5,4,100,7,10,6,11,17,13,90,22]
print("최대값:",fmax(su))
