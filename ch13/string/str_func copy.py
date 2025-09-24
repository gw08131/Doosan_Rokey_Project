# str_func.py

my_string = 'Python is a popular programming language.'
split_list = my_string.split()
print(split_list)
#['Python', 'is', 'a', 'popular', 'programming', 'language']
# 띄어쓰기 별로 하나씩 잘림


my_string1 = "Python,is,a,popular,programming,language."
split_list1 = my_string1.split(",")
print(split_list1)
# 구분하는 형태는 다양하게 할 수 있음
# 스플릿을 한 특정 단어로도 할 수 있음!

print("-------------------------")
my_string2 = '''Python programability on 
                Algoran makes the entire development 
                lifecycle easier and means more afforable and 
                efficent maintenance and upgrades 
                going forawrd.'''
slit_list2 = my_string2.split('\n')
print(slit_list2)

print("-------------------------")
my_string = "   Python is awesome!   "
stripped_string = my_string.strip()
print(my_string +'a')           #   Python is awesome!   a
print(stripped_string +'a')     #Python is awesome!a


print("-------------------------")
#이스케이프 (escape) 코드: 미리 강의해 둔 문자조항
#\n = newline
#\t = tap
#\b = backspace
#\' = 작은 따옴표 표시
#\" = 큰 따옴표 표시
#\r = 커서를 현재 줄의 가장 앞으로 이동

print("-----------------")
my_list = ['apple','banana', 'charry']
#joined_string = "-".join(my_list)
joined_string = "\n".join(my_list)
joined_string = "\t".join(my_list)
joined_string = "\b".join(my_list)
print(joined_string)