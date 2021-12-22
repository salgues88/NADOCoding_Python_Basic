# __init__.py 파일은 해당 폴더 내의 .py 파일이 패키지의 일부임을 인식하는 기능
# (디렉토리에 __init__.py 파일이 없으면 패키지로 인식 안됨)


from .cat import Cat                            # . <- "이 폴더에 있는" cat.py라는 파일에서 Cat이라는 클래스를 가지고 와줘 

from .dog import Dog                            # . <- "현재 폴더에 있는" dog.py라는 파일에서 Dog 클래스를 가지고 와줘

#from .cat import *                             # 현재 폴더에 있는 cat.py내의 모든 클래스를 가지고 와줘





# __all__ = ["cat", "dog"]

# 특정 디렉토리 내의 모듈들의 모든 클래스를 *를 이용하여 import 할 때 사용
# (개별로 부르고 싶으면 'from 이름.py import class이름' 으로 부르면 됨)