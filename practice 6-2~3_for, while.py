# 반복문 (loop)


# [테크보이 워니 설명] https://www.youtube.com/watch?v=M6kQTpIqpLs&ab_channel=TeccboiWonie

# 반복문에는 for 과 while 2가지가 있음

for i in range(5):                              # i : x번째, range(5) : 5번 반복
  print(i)                                      # i는 0부터 시작함
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야 그냥 있어")




# (번외) 반복문을 합치는 기능 (매우 중요한 컨셉!! by 테크보이 워니)
print("\n")

x = [4, "hello", 3, "world"]

for n in x:                                     # n 내부에 x 리스트 내부 요소들이 1번씩 번갈아 가면서 출력됨
    print(n)

print("\n")
print(x.index(3))                               # x 리스트 내부 요소 중 숫자 3이 어디에 있는지 찾는 기능
print(x.index("hello"))                         # x 리스트 내부 요소 중 문자 hello가 어디에 있는지 찾는 기능

print("hello" in x)                             # x 리스트 내부 요소 중에 문자 hello가 있는지 확인 (True/False)

if "bye" in x:                                  # x안에 bye가 없기 때문에 아무것도 안뜸
    print("bye가 있어요")

print("\n")




# [나도코딩 설명] 

# 6-2 for (리스트 or 튜플 or 문자열의 처음 요소부터 마지막 요소를 순차적으로 반복 출력)

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")


# 대기손님이 100명이 되서 번호가 100번까지 된다면? -> 이 떄 for를 씀


# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5):                                 # range(숫자) : 0~ 해당 숫자 미만의 정수값 생성
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 5):                              # ragne(숫자1, 숫자2) : 숫자1 ~ 숫자2 미만의 정수값 생성
    print("대기번호 : {0}".format(waiting_no))



starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되어 있습니다".format(customer))



# 번외. 리스트, enumerate 기능 사용 방법 
print("\n")
lst = ["가", "나", "다"]

for lst_idx, lst_val in enumerate(lst):                     # for index, value in enumerate(변수): 인덱스 값을 추가해서 반복문의 번호를 표시함 (range 함수와 비슷함)
    print(lst_idx, lst_val)                                 





#################################################################################################################




# 6-3 while (어떤 '조건'을 만족할 떄 까지 반복) (while과 for의 차이는 조건을 달 수 있냐 없냐임)

# [테크보이 워니 설명] https://www.youtube.com/watch?v=M6kQTpIqpLs&ab_channel=TeccboiWonie

print("\n")

i = 0
while i <3:                                                                 # 일반적인 while 조건은 끝이 있음
  print(i)
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야 그냥 있어")
  i = i + 1                                     # i = 0 + 1

# for과 while은 둘 다 교차 사용 가능하고 보통 사용하기 편한 방향으로 반복문을 사용함


print("\n")




# [나도코딩 설명]

customer = "라쿤"
index = 5
while index >= 1:
    print("{0} 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1                                              # a -= b 는 a = a-b             # 35~38번이 계속 반복됨
    if index == 0:                                          # == : 앞과 뒤의 값이 똑같음     # if 문장
        print("커피는 폐기 처분 되었습니다")


# customer2 = "아이언맨"
# index2 = 1
# while True:
#     print("{0} 커피가 준비되었습니다. 호출 {1}회 남았어요.".format(customer2, index2))
#     index2 += 1

# 무한 루프에 빠졌을 때는 출력창 클릭 후 Ctrl +C 눌리면 됨



customer3 = "토르"
person = "Unknown"

while person != customer3:
    print("{0} 커피가 준비되었습니다.".format(customer3))
    person = input("이름이 어떻게 되세요? ")





