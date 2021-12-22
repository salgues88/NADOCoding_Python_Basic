# 6-4 continue와 break


# [테크보이 워니 설명]

# continue : 반복문에서 보통 if와 같이 사용해서 continue 조건에 해당되거나
#            (또는 continue 단독으로만 사용 시) continue 밑의 문장은 패스하고 다음 반복문 실행 (일종의 skip 기능)

# break : 반복문에서 보통 if와 같이 사용해서 (무한)루프를 강제 종료 하는 기능

# while의 경우 무한 루프에서 자주 사용
i = 0
while True:                                                             # True 는 절대로 안변함 (불변 조건)
    print(i)
    print("철수 : 안녕 영희야 뭐해?")
    print("영희 : 안녕 철수야 그냥 있어")
    i = i + 1    

    if i > 5:                                                           # 무한루프 끊는 방법
        break



for i in range(5):                                                      # i : x번째, range(5) : 5번 반복
  print(i)                                                              # i는 0부터 시작함
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야 그냥 있어")

  if i > 3:                                                             # i가 3보다 크면 반복문 멈춤
      break



for i in range(5):                                           
  print(i)                                                             
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야 그냥 있어")

  if i == 3:                                                            # i가 3 일 때 continue 밑의 문장 스킵
      continue

  print("continue 비활성화 상태")


print("\n")



# [나도코딩 설명]

absent = [2, 5]                             # 결석
no_book = [7]                               # 책을 깜빡함
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 끝났다. {}은 교무실로 따라와라".format(student))
        break                                                           # (무한)루프를 돌다가 중간에 끝내고 싶을 떄 사용
    print("{0}아 책을 읽어봐".format(student))


print("\n")




#################################################################################################################

print("\n줄 바꿈\n")


# 6-5 한줄 for (리스트와 함께 쓰임)

# 출석번호가 1, 2, 3, 4가 있는데 앞에 100을 붙이기로 함 (101, 102, 103, 104)
students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]                                    # i + 숫자 for i in 변수
print(students)

print("\n줄 바꿈\n")

# 학생들 이름을 길이로 변환
students = ["Iron Man", "Thor", "I am Groot"]
print(students)

students = [len(i) for i in students]                                   # len() : 문자열 숫자 개수를 정수로 표시 
print(students)                                                         # 한줄 for는 4-3 문자열 처리함수와 자주 쓰임


print("\n줄 바꿈\n")

# 학생들 이름을 대문자로 변환
students = ["Iron Man", "Thor", "I am Groot"]
print(students)

students = [i.upper() for i in students]
print(students)




#################################################################################################################




# Quiz 5.당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다
# 조건2 : 당신은 소요시간 5~15분 사이의 승객만 매칭해야 합니다

# (출력문 예제)
# [0] 1번쨰 손님 (소요시간 : 15분)
# [ ] 2번쨰 손님 (소요시간 : 50분)
# [0] 3번쨰 손님 (소요시간 : 5분)
# ...
# [ ] 50번쨰 손님 (소요시간 : 16분)
# 총 탑승 승객 2분


print("\n줄 바꿈\n")


# 해답 1 (나도코딩)

from random import *

cnt = 0                                                           # 총 탑승 승객 수

for i in range(1, 51):                                            # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51)                                       # 5 ~ 50분 소요시간
    if 5 <= time <= 15:                                           # 5 ~ 15분 이내의 시간, 탑승 승객 수 증가 처리
        print("[0] {0} 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:                                                         # 매칭 실패한 경우
        print("[ ] {0} 손님 (소요시간 : {1}분)".format(i, time))


print("총 탑승 승객 : {0}분".format(cnt))







# 해답 2 (나)   (못품...)

# from random import *

# for customers in range(1, 51):
#     print("{0}번째 손님 (소요시간 : {1}분)".format(customers, randint(5, 51)))
#     print("총 탑승 승객 {}분".format())
    