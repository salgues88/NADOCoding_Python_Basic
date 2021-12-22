# 자료구조의 변형
# ex. 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))                             # 자료구조를 변수, tyle(변수)로 확인한 결과, 출력값에 <class 'set'>

menu = list(menu)                                   # 자료 구조를 list로 변경
print(menu, type(menu))                             # 자료구조를 변수, tyle(변수)로 확인한 결과, 출력값에 <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) 

menu = set(menu)
print(menu, type(menu))







# Quiz 4. 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.

# 참석율을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.

# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 추첨 프로그램을 작성하시오


# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --


# 활용 예제
# from random import *                  # 밑의 shuffle 함수가 random에 속하므로 해당 문장이 반드시 필요함
# lst = [1, 2, 3, 4, 5]
# print(lst)

# shuffle(lst)
# print(lst)

#print(sample(lst, 1))











# 해답1 (나도코딩 강사)
from random import *
users = range(1, 21)                    # range(1, 21) : 1 ~ 20 까지 숫자 생성
#print(type(users))                     # range는 타입이 range -> list로 변경 필요
users = list(users)                     # 타입을 list로 변경
#print(type(users))
print(users)

shuffle(users)                          # shuffle은 'random' 함수에 포함되므로 사용 시 앞에 from random inport * 를 붙여야함
print(users)

winners = sample(users, 4)              # 4명 중에서 1명은 치킨, 3명은 커피 쿠폰
print(winners)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")




# 해답 2 (내가 코딩한 값)

from random import *
users = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(users)
shuffle(users)
print(users)

print("-- 당첨자 발표 --\n치킨 당첨자 : " + str(users[0]) + "\n커피 당첨자 : " + str(users[1:4]) + "\n-- 축하합니다 --")


