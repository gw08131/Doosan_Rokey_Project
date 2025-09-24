# p3.py

with open("계좌1.txt", "w", encoding="utf-8") as f:
    f.write("김삿갓 597-89-000089\n이수근 343-64-000064\n박혁거세 136-97-000097")
print(f.closed)

path = r"C:\rokey\python\계좌1.txt"
mode = "r"
with open(path,mode,encoding="utf-8") as f:
    lines = f.readlines()

account_dict = {}
for line in lines:
    lineList = line.split() #공백을 기준으로 분리
    #lineList[0] → 예금주 이름, lineList[1] → 계좌번호
    account_dict[lineList[0]] = lineList[1]
    #account_dict["김삿갓"] = "597-89-000089"

for key, val in account_dict.items():
    print(f"{key}: {val}")    


