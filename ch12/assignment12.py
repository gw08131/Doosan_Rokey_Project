# assignment12.py

with open("pizza_file1.txt","w",encoding="utf-8") as file:
    file.write("페퍼로니피자\n치즈피자\n콤비네이션피자")
print(file.closed)

with open("pizza_file1.txt","w",encoding="utf-8") as file:
    file.write("페퍼로니피자 3000\n치즈피자 3200\n콤비네이션피자 3500")
print(file.closed)

with open("pizza_file1.txt","a",encoding="utf-8") as file:
    file.write("\n불고기피자 3600\n해산물피자 3800")
print(file.closed)

f = open("pizza_file1.txt","r",encoding="utf-8")
print(f.read())
f.close()

f = open("pizza_file1.txt","r",encoding="utf-8")
pizza_lst = []
for line in f:
    pizza_lst.append(line)
print(pizza_lst)
f.close()

path = r"C:\rokey\python\pizza_file1.txt"
f = open(path,"r")
lines = f.readlines()
for line in lines:
    print(line,end=" ")
f.close()