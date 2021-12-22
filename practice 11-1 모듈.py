# 11-1 모듈 : 소프트웨어도 부품 추가/교체 처럼 사용하는 기능


# [테크보이 워니 설명] https://www.youtube.com/watch?v=M6kQTpIqpLs&ab_channel=TeccboiWonie

# 패키지 : 어떤 기능들을 구현하는 모듈들의 합 (ex. 날씨, 위치 등등등)

# 라이브러리 == 패키지 (다른데서 라이브러리라고 하는걸 파이썬에서는 패키지라고 함)

# 모듈 == 코드가 들어있는 파일 (이 코드들이 모여서 어떤 한 기능을 구현함)

# 모듈은 코드를 다른 사람들과 공유하거나, 코드를 잘 정리하기 위해서 모듈화해서 사용 

# 모듈, 패키지를 공부한 이후에는 다른 사람이 만든 코드를 가져와서 사용 가능!!!


# 테크보이 워니 패키지, 모듈 예제 예제

# animal package
# dog, cat module
# dog, cat modules can say "hi"


# 패키지를 만들려면 먼저 폴더를 하나 만들어야 함 (animal 폴더)
# -> 폴더 내에 dog.py, cat.py 작성 및 내용 입력 (이때 cat, dog가 모듈)
# -> anmial 폴더가 패키지라고 말을 하고 싶으면 __init__.py 파일을 생성해야 함 (해당 디렉토리가 패키지임을 정의)


# animal 디렉토리에 __init__.py, cat.py, dog.py 파일 다 만든 후

# from animal import dog                                        # animal 패키지에서 dog라는 모듈을 가지고 와줘
# from animal import cat

# from animal.dog import Dog                                    # animal 패키지 내 dog 모듈에서 Dog 클래스를 불러와줘

# d = dog.Dog()
# d.hi()

# c = cat.Cat()
# c.hi()

# 위 방식은 반복이 많이됨 -> 코드 축약 추천

from animal import *                                            # animal 패키지에서 모든 모듈을 가지고 와줘

d = Dog()                                                       # *로 호출 시 모듈명 적을 필요 없이 class 이름만 적으면 됨
c = Cat()

d.hi()
c.hi()

# 다른 사람이 작성한 라이브러라 가져와서 사용 예시      (해당 예시는 repl.it 사이트 가서 따라할것!)
# geocord (https://geopy.readthedocs.io/en/stable/)

# repl.it 사이트에서 왼쪽 탭의 package 클릭 -> search (geopy) -> geopy 눌러서 인스톨
# -> geocord의 예시 복사, 붙여넣기


# 남이 만들어 놓은 코드 가져와서 사용할 땐 설명서 읽는 것도 좋지만,
# 코드를 가져와서 실행해보고, 왜 이렇게 작성했는지를 분석하는 것이 더 중요!


print("\n")




# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

# theater_module.py 파일 생성해서 내용 입력함

print("[다른 .py 파일 불러올 때 사용하는 방법 1]")
import theather_module                                          # 다른 .py 함수를 불러오는 기능
theather_module.price(3)                                        # 3명이 영화보러 갔을 때
theather_module.price_morning(4)
theather_module.price_soldiers(5)



print("\n[다른 .py 파일 불러올 때 사용하는 방법 2]")               # 불러오는 파일 이름이 길 때 'as 새명칭'으로 리네이밍 
import theather_module as mv                                      
mv.price(3)
mv.price_morning(4)
mv.price_soldiers(5)



print("\n[다른 .py 파일 불러올 때 사용하는 방법 3-1]")            # from 불러올파일이름 import *
from theather_module import *                                   # * : 불러올 파일 내의 모든 함수를 불러옴
price(3)                                                        # 이 방식은 앞에 다른파일이름을 안적어도 됨
price_morning(4)
price_soldiers(5)



print("\n[다른 .py 파일 불러올 때 사용하는 방법 3-2]")
from theather_module import price, price_morning                # 불러올 파일 내의 특정 함수만 불러오는 방법
price(5)
price_morning(10)
# price_soldiers(2)                                             # price-soldiers는 불러오지 않았으므로 오류 발생



print("\n[다른 .py 파일 불러올 때 사용하는 방법 3-3]")
from theather_module import price_soldiers as ps               # 특정 함수만 불러온 후 특정 함수 이름 리네이밍
ps(5)


