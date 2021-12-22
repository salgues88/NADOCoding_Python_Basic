# 8-1 표준 입출력

# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

print("Python", "Java", "C", sep = " vs ")          # ,는 디폴드 값이 1칸 띄우기 -> sep를 이용해서 ""사이값을 입력하면 전체 적용

print("Python", "Java", "C", sep = " : ", end = "? ")   # , 뒤에 end를 사용하면 ""내의 값이 맨 마지막 출력값에만 적용 및 
print("무엇이 출력될까요\n")                                #   밑의 문장을 한문장으로 연결

# print("Python", "Java", file = sys.stdout)                    # stdout : 표준출력
# print("Python", "Java", file = sys.stderr)                    # stderr : 에러


scores = {"수학" : 0, "영어" : 50, "코딩" : 100}                 # 5-2 사전 기능
for subject, score in scores.items():                           # 변수.items() : 변수 내 key, value 값 모두 출력
    # print(subject, score)                                     # 변수.ljust(숫자) : 왼쪽부터 칸 수 띄우기              
    print(subject.ljust(8), str(score).rjust(4), sep = ":")     # int() : 정수로 만듬



# 은행 대기순번표
# 001, 002, 003, ...
print("[은행 대기순번표 예시]")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))                     #zfill(숫자) : 몇자리 수의 빈공간을 0으로 채우는 기능

answer = input("아무 값이나 입력해 주세요 : ")
print("입력하신 값은 " + answer + " 입니다")