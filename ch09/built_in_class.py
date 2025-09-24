# build_in_class.py

# class int:
#     #정수 변환 기능
#     def __init__ (self,data):
#         self.data = data
# na = 10
# na = "10"
# na = int(10)

stra = "abc"
print(stra)
print(type(stra))       #<class 'str'>

strb = stra("abc")
print(strb)
strc = strb.capitialize()       #strb가 클래스이기때문에 접근연산자 .capitalize()가 가능함!
print(strc)