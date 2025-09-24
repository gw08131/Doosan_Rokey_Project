# p2.py

with open("계좌1.txt", "w", encoding="utf-8") as f:
    f.write("김삿갓 597-89-000089\n이수근 343-64-000064\n박혁거세 136-97-000097")
print(f.closed)

path = r"C:\rokey\python\계좌1.txt"
mode = "r"
with open(path,mode,encoding="utf-8") as f:
    lines = f.readlines()

account_list = []
for line in lines:
    #print(line)
    lineList = line.split() #공백을 기준으로 분리
    account_list.append(lineList[1])
    print(account_list)     


