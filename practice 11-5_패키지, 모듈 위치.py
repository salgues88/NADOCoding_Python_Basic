# 11-5 패키지, 모듈 위치

# 패키지와 모듈은 정해진 위치에 있어야 에러 없이 가용 가능
# -> 패키지와 모듈이 어느 위치에 있는지 확인하는 방법 필요

import inspect                                              # 패키지, 모듈 위치 찾는 구문
import random                                               
print(inspect.getfile(random))                              # 랜덤 파일 위치 표시

# 실행 -> C:\Python38\lib\random.py 위치에 random 존재 확인


# 패키지 내 모듈 위치 파악 방법
from travel import *                                        # travel 패키지 호출 구문
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))                            # travel 패키지 내 thailand 모듈 위치 표시

# 실행 -> c:\Users\9\Desktop\PhythonWorkSpace\travel\thailand.py 위치에 thailand 존재 확인