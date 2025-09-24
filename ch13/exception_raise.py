#exception_raise.py

try:
    raise NameError("HiThere")          #raise는 지정한 예외가 발생하도록 강제 
except NameError as e:
    print("NAmeError: 예외 발생!")
    print(e)            #HiThere <- 애 때문에 NameError발생