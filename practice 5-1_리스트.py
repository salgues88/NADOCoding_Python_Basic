# 자료구조 : 리스트, 튜플, 딕셔너리, 세트


# [테크보이 워니 설명] https://www.youtube.com/watch?v=M6kQTpIqpLs&ab_channel=TeccboiWonie

# 리스트 : 엘레멘트 여러개를 그룹핑할 때 사용

x = list()
y = []                                                  # 리스트는 대괄호

print(x)
print(y)

# 리스트 사용 예시

x = [1, 2, 3, 4]                                        
y = ["hello", "world"]
z = ["hello", 1, 2, 3]

print(x[0])                                             # 프로그래밍은 항상 0부터 시작함 -> 0자리값 = 리스트 첫번째 값
print(x + y)
print(x + z)

x[3] = 10                                               # x변수의 3번째 자리값을 10으로 변경
print(x)

num_element = len(x)                                    # x 내 요소가 총 몇개인지 확인
print(num_element)


print("\n")




# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)


subway = ["유재석", "조세호", "박명수"]                  # 리스트는 변수 = [] 형태임
print(subway)

# 조세호 씨는 몇 번쨰 칸에 타고 있는가?
print(subway.index("조세호"))                           # 행렬도 0부터 시작


# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")                                   # 변수.append("문자열") : 리스트 맨 뒤에 문자열 추가
print(subway)


# 정형돈씨를 유재석씨와 조세호씨 사이에 태움
subway.insert(1, "정형돈")                              # 변수.insert(위치숫자, "문자열") : 문자열을 행렬 사이에 넣을 떄 사용
print(subway)


# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
subway.pop()                                            # 변수.pop : 맨 뒤의 문자열을 밖으로 꺼냄
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)


# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)

print(subway.count("유재석"))                            # 변수.count("문자열") : 변수 내에 문자열이 몇 개 있는지 카운트



# 정렬
print("\n")
num_list = [5, 2, 4, 3, 1]
num_list.sort()                                         # 변수.sort() : 변수 내 무작위 숫자를 순서대로 정렬
print(num_list)

s = sorted(num_list)                                    # sort 기능을 이렇게도 표현 가능
print(num_list)



# 순서 뒤집기
print("\n")
num_list.reverse()                                      # 변수.reverse() : 변수 내 무작위 숫자를 역순으로 정렬
print(num_list)



# 모두 지우기                                           # 변수.clear() : 변수 내 숫자들 모두 삭제
print("\n")
num_list.clear()
print(num_list)



# ※ '변수.reverse()' vs 'reversed(변수)'        (practice 5-1_리스트.py 참고)
###    - 변수.reverse() : 변수 내 무작위 숫자를 역순으로 정렬 (순서 영구 변경)
print("\n")
lst = [1, 2, 3, 4, 5]
print(lst)                              # 기존 lst 출력값      : [1, 2, 3, 4, 5]
lst.reverse()
print(lst)                              # lst.reverse() 출력값 : [5, 4, 3, 2, 1] (요소 순서가 영원히 뒤바뀜)

###    - reversed(변수) : 변수 내 무작위 숫자 순서는 그대로이나, 다음 변수에는 역순값을 전달함  (기존변수 순서변경 X, 뒤집힌 값이 다른 변수에 전달됨)
print("\n")
lst2 = [1, 2, 3, 4, 5]
print("lst2 뒤집기 전 :", lst2)         # 기존 lst2 출력값 (lst2 뒤집기 전)      : [1, 2, 3, 4, 5]

lst3 = reversed(lst2)
print("lst2 뒤집기 후 :", lst2)         # reversed(lst2) 출력값 (lst2 뒤집기 후) : [1, 2, 3, 4, 5] (lst2 요소 순서 변경 X -> 실제 lst2 값에는 영향 없음)
print("리스트3 :", list(lst3))          # lst3 출력값 (lst2 뒤집기 후 전달 받은값) : [5, 4, 3, 2, 1] (뒤집한 lst2 값이 lst3로 전달)


# 리스트는 다양한 자료형 함꼐 사용 가능
print("\n")
mix_list = ["조세호", 20, True]
print(mix_list)

num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]



# 리스트 확장
num_list.extend(mix_list)                               # 변수.extend(변수) : 변수 2개의 값을 합치는 기능  
print(num_list)