# find_min.py

su = [5,4,7,10,6]
def fmin(fu):
    min_val = fu[0]
    for i in range(1,len(fu),1):
        if min_val > fu[i]:
            min_val = fu[i]
    return min_val

mina=fmin(su)
print("최소값 mina는 ", mina)