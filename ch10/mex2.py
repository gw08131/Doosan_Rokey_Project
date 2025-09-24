# mex2.py

import mex1

p2 = mex1.Cvalue()
p2.add(11)
p2.add(21)
p2.add(31)
p2.fprint()

#함수
value = mex1.plus(10,20)    #class 외부의 함수 가져오기
print(value)

#변수
print(mex1.str1)
mex1.str = "hi"
print(mex1.str1)

mex1.p1.lista.append(4)
mex1.p1.fprint()

print("----------------------------")

import sample.mex11

crossbag = sample.mex11.Bag()
crossbag.add("텀블러")
print(crossbag.data)

