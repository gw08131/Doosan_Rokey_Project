# mex3.py
#먼저 실행한 모듈 => 불러온 모듈

# import 모듈명
# from 모듈명 import 함수
# from 모듈명 import *

from mex1 import Cvalue     #클래스 불러오기
from mex1 import plus       #함수 불러오기
from mex1 import p1         #객체 불러오기

from mex1 import *          # mex1의 내용 모두 불러오기

# mex1.plus()
sum = plus(11,22)
print(sum)