# func3.py
def fadd(pa, pb):
    return pa + pb

def fsub(pa, pb):
    return pa - pb

def fmul(pa, pb):
    return pa * pb

def fdiv(pa, pb):
    return pa / pb

na = 100
nb = 3

nc = fadd(na, nb)
print(na, "+", nb, "=", nc)
nc = fsub(na, nb)
print(na, "-", nb, "=", nc)
nc = fmul(na, nb)
print(na, "x", nb, "=", nc)
nc = fdiv(na, nb)
print(na, "/", nb, "=", nc)


print("-----------------------")
def fadd(pa, pb):
    return pa + pb

def fsub(pa, pb):
    return pa - pb

def fmul(pa, pb):
    return pa * pb

def fdiv(pa, pb):
    if pb == 0:
        return "0으로는 나눌 수 없다."
    else:
        return pa / pb

na = float(input("첫번째 숫자: "))
nb = float(input("두번째 숫자: "))

nc = fadd(na, nb)
print(na, "+", nb, "=", nc)
nc = fsub(na, nb)
print(na, "-", nb, "=", nc)
nc = fmul(na, nb)
print(na, "x", nb, "=", nc)
nc = fdiv(na, nb)
print(na, "/", nb, "=", nc)

print("-----------------------")
def string_length(stb):
    count = 0
    for chara in stb:
        count = count+1
    return count

sta = "python example"
lena = string_length(sta)
print(lena)
