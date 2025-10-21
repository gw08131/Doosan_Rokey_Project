# Q20-9.py

# 9. Scipy의 root 함수를 사용하여 
# 방적식 (x−3)^2 = 0 의 근을 구하시오.

from scipy.optimize import root

def equation(x):
    return (x-3)**2

result = root(equation,x0=0)
print(result.x)