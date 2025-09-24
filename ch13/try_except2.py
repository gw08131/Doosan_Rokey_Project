# try_except2.py

# f = open('myfile.txt')      #FileNotFoundError:
# s = f.readline()
# i = int(s.strip())

try:
    path = r"ch13\exception\myfile.txt"
    #f = open('myfile.txt')      #mode 기본값은 r
    #f = open(path,'w')
    f = open(path)
    s = f.readline()
    i = int(s.strip())
except(RuntimeError, TypeError, NameError):
    print("RuntimeError, TypeError, NameError 중 하나의 예외가 발생시 처리 구문") 
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except OSError as err:  
    print("OS Erro:",err)           #s=f.readline()인데 txt에 내용이 없어서 not readable 오류 뜸
except ValueError:
    print("정수형으로 변환할 수 없습니다.")     # 정수
except Exception as e:
    print(f"Unexpected {e}, {type(e)}")