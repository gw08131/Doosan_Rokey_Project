# default1.py

#def 함수명 (매개변수1 = 기본값1, 매개변수2 = 기본값2, ...)
#    코드블록
#    return 반환값
#함수명()
def persona(width = 11, height = 21):
    print("함수디폴트값없음, width = ", width, "height = ", height)

def personb(width=4, height=3):
    print("함수디폴트값설정, width = ", width, "height = ", height)

persona(10,20)    #인수가 우선순위가 높다. 
# 그래서 디폴트값이 있어도 인수가 (10, 20)으로 설정되어있어서 출력은 10,20으로 나옴

#persona()        #input 인수 두개를 넣어야하는데 빈칸이라 오류
personb()

# 부분 매개변수에 기본값 설정시, 뒤에서부터 설정
def persona(width, height = 21):
    print("width = ", width, "height = ", height)

# 문법적 오류
#def persona(width=11, height):
#    print("width = ", width, "height = ", height)
#persona(20)

print("-----------------------------------")
def persona(width=20, height = 21, weight = 57):
    print("함수 기본값 있음")
    print("width = ", width, "height = ", height, "weight = ", weight)
    print("width = ", width)
persona()
persona(30)
persona(30,180)
persona(30, 180, 50)

#1. 모든 매개변수에 기본값 설정 가능
#2. 부분 매개변수에 기본값 설정시, 뒤에서부터 설정
#3. 기본값에 있더라도 인수 전달 가능 (전달된 인수의 우선 처리)


range(0,10)
range(0,10, step=1)

print("hello")
print("hello", end="\n")