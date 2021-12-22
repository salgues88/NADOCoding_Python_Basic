# 5-2 사전 (딕셔너리)

# [테크보이 워니 설명]

x = dict()
y = {}                                                           # 사전은 중괄호

print(x)
print(y)

# 사전(dictionary)은 변수 = {key : value} 형태로 중괄호 내의 내용을 더하고 빼기 가능

# key(=index (?))는 불변하는 값(문자열, 숫자열 등)만 사용 가능 

# 사전 구조는 아주 유용하고, 매우 자주 쓰임

x = {
    "name" : "워니",
    "age" : 20,
    0: "hello",
    1: "world",
}

print("\n")
print(x)                                                         # x 사전 내 모든 요소 표시 (키, 밸류 포함)
print(x["name"])                                                 # x 사전 내 "name" 키에 해당되는 밸류값이 표시됨
print(x["age"])                                                  # x 사전 내 "age" 키에 해당되는 밸류값이 표시됨
print(x[0])

print("\n")

for key in x:
    print("key : " + str(key))                                   # for 반복문으로 key 값들을 하나씩 출력
    print("value : " + str(x[key]))                              # for 반복문으로 x 사전 value 값들 하나씩 출력
#                    여기서는 key, value 값이 출력된 후 문자로 만들어야 하므로 "" 사용 불가!

x[0] = "수호랑"                                                  # x 사전 내 0 키값 변경 ("hello" -> "수호랑")
print(x)

x["school"] = "한빛"                                             # x 사전 내 기존에 없는 키, 밸류값 추가
print(x)




# 자료구조 예제 (by 테크보이 워니) (사전이 어떻게 활용되는지를 보여주는 예제)

# fruit 변수 내에 각 과일이 몇 개씩 있는지 찾을 수 있는 프로그램 짜기

fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]






# 해답1 (테크보이 워니) (정말 깔끔한 코드!!!)
print("\n")
d = {}                                                          # d는 사전 이다 라고 정의

for i in fruit:                                                 # i 에 맨 처음에 "사과"가 투입
    if i in d:                                                  # "사과"라는 키가 d라는 사전에 들어있는지?
        d[i] = d[i] + 1                                         # 들어있으면 개수를 1개 올려줘
    else:
        d[i] = 1                                                # 만약 "사과"라는 애가 없으면 사전에 넣고 값은 1로 만들어줘
print(d)                                                        # ("사과"라는 키가 없으므로 사과 키를 생성하고, 밸류는 1)



# 해답2 (나) (count 함수를 이용하여 값 세기)
# print(fruit.count("사과"))


print("\n")




# [나도코딩 설명]

print("\n")
cabinet = {3 : "유재석", 100:"김태호"}                            # 3 - key, "유재석" - value


# 설정한 value 값을 표현하는 방법 1
print(cabinet[3])
print(cabinet[100])
# print(cabinet[5])                                              # 변수[] 사용 시 대괄호에 변수 내에 없는 값을 입력 시 
print("Hi")                                                      #  그 아래의 모든 연산이 멈춤

# 설정한 value 값을 표현하는 방법 2 
print(cabinet.get(3))
print(cabinet.get(100))
print(cabinet.get(5))                                            # 변수.get() 사용 시 괄호에 변수 내에 없는 값이 입력 시
print("Hello")                                                   #  None이라고 뜨면서 아래 연산 가능

print(cabinet.get(5, "사용가능"))                                # 변수.get(키 숫자, "문자열") 시 변수에 해당 키가 없으면 자동으로 value 생성
print("Hello World")

 
# 키가 변수 안에 있는가 확인 (결과는 boolean으로 표시)
print(3 in cabinet)
print(5 in cabinet)



# Key는 정수, 문자열(str) 둘 다 사용 가능 (정확히는 불변하는 값 사용가능)
cabinet2 = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])
print(cabinet2.get("A-3"))
print(cabinet2.get("B-100"))

# 목욕탕 새 손님
print(cabinet2)                                                  # 현재 변수 cabinet2의 값 확인
cabinet2["A-3"] = "김종국"                                       # 기존 key 값 내의 기존 value 덮어쓰기 ("유재석" -> "김종국")
cabinet2["C-20"] = "조세호"                                      # 기존에 없던 key, value 값 추가
print(cabinet2)

# 목욕탕 간 손님
del cabinet2["A-3"]                                             # 변수 내 key 삭제
print(cabinet2)


# 변수 내 Key 들만 출력하는 방법
print(cabinet2.keys())                                          # 변수.keys() : 변수 내 key 값들만 출력

# 변수 내 value 들만 출력하는 방법
print(cabinet2.values())                                        # 변수.values() : 변수 내 value 값들만 출력

# 변수 내 key, value값 동시 출력
print(cabinet2.items())                                         # 변수.items() : 변수 내 key, value 값 모두 출력


# 목욕탕 폐점 (=key, value 삭제)
cabinet2.clear()
print(cabinet2)
