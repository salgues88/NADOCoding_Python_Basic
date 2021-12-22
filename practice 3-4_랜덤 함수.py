

# from random import *            # 랜덤 함수 사용하기 전에 반드시 해당 문장을 맨 먼저 적어야 함

# print(random())                 # random() : 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10)            # ramdon() * 10 : 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10))       # int(ramdon() * 10) : 0 ~ 10 미만의 임의의 값 생성 
# print(int(random() * 10))       # int : 숫자열, 문자열 -> 정수형으로 변환
# print(int(random() * 10))
# print(int(random() * 10) + 1)   # random() * 10) + 1 : 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) 
# print(int(random() * 10) + 1) 
# print(int(random() * 10) + 1) 
# print(int(random() * 10) + 1) 

# print(int(random() * 45) + 1)     # int(random()) * 45 + 1 : 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1, 46))             # randrange(1, 46) : 1 ~ 46 미만의 임의의 정수값 생성 
# print(randrange(1, 46))             # randrange(1, 46) : 1 ~ 45 이하의 임의의 정수값 생성
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))

# print(randint(1, 45))               # randint(1, 45) : 1 ~ 45 이하의 임의의 정수값 생성
# print(randint(1, 45))   
# print(randint(1, 45))   
# print(randint(1, 45))   
# print(randint(1, 45))   
# print(randint(1, 45))   




# Quiz 2. 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디 하는데 3회는 온라인으로, 1회는 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월 별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

# 출력문 예제 : 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.









from random import *
date = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")