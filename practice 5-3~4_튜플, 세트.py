# 5-3 튜플                                             #튜플은 내용 추가나 변경을 할 수 없음. 대신 속도가 빠름

# [테크보이 워니 설명]

# 리스트와 튜플의 가장 큰 차이점
# : 튜플에서는 Assignment 불가 (Assignment : 튜팔 안의 값을 업데이트 하는것) = 불변(immutable), 값을 바꿀 수 없음
#   (리스트 : 가변(mutable), 값을 바꿀 수 있음)

x = tuple() 
y = ()                                                 # 튜플은 소괄호    

print(x)
print(y)

x = (1, 2, 3)
y = ("a", "b", "c")
z = (1, "hello", "world")

print(x + y)
print(z.index(1))                                      # z 튜플 내의 요소가 어느 위치에 있는지 표시하는 방법
print("a" in y)                                        # y 튜플 내에 문자열 a가 있는지 확인 (True / False)

# x[0] = 2                                             # TypeError: 'tuple' object does not support item assignment


print("\n")




# [나도코딩 설명]

menu = ("돈까스", "치즈까스")                           # 튜플은 변수 = () 형태임
print(menu[0])
print(menu[1])

#menu.add("생선까스")                                   # 튜플은 값을 더하거나 뺴기 불가


name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)


(name, age, hobby) = ("김종국", 20, "코딩")             # 튜플은 변수를 쭉 나열해서 표현 가능
print(name, age, hobby)


print("\n")




# [나도코딩 설명]

# 5-4 세트                                              # 사전과 동일하게 중괄호{} 사용 (대신 key와 value 관계는 없음)
# 집합(set), 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)                                           # 세트는 중복 허용 안됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])                       # 세트는 변수 = {} 및 변수 = set([]) 2가지 형태로 표현 가능


# 교집합 (Java와 Python 모두 할 수 있는 개발자)           # 교집합 : 변수 & 다른 변수   또는   변수.intersection(다른 변수)
print(java & python)
print(java.intersection(python))

# 합집합 (Java 또는 Python을 할 수 있는 개발자)           # 합집합 : 변수 | 다른 변수   또는   변수.union(다른변수)
print(java | python)
print(java.union(python))                               # 출력값이 랜덤임 (∵ 세트는 원래 순서가 없음)

# 차집합 (Java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")                                    # python.add(문자열) : 변수 내 문자열 추가
print(python)

# java를 까먹은 사람이 나타남                            # python.remove(문자열) : 변수 내 문자열 제거
java.remove("김태호")
print(java)

