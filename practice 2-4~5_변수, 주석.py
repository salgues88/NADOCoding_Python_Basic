# 2-4 변수

# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

# 애완동물을 소개해 주세요
animal = "고양이"               # animal : 변수 지정 
name = "아옹이"                 # name : 변수 지정
age = 2
hobby = "뒹굴기"
is_adult = age >= 3



# print("우리집 고양이의 이름은 아옹이 입니다")
# print("아옹이는 2살이고 뒹굴기를 좋아합니다")
# print("아옹이는 어른일까요?")



print("우리집 " + animal + "의 이름은 " + name + " 입니다")
name = "해피"
# name이 2개면 바뀐 name 순서 밑으로 이름이 변경됨
print(name + "는 " + str(age) + "살이고 " + hobby + "를 좋아합니다")
print(name + "는 어른일까요? " + str(is_adult))

# '+'를 사용 시 문자열은 그대로, 숫자열은 str() 안아 감싸야 함



print("우리집 ", animal, "의 이름은 ", name, " 입니다")
print(name, "는 ", age, "살이고 ", hobby, "를 좋아합니다")
print(name, "는 어른일까요? ", is_adult)

# ','를 사용 시 문자열은 그대로, 숫자열도 그대로 사용, 그리고 콤마 사용 시 뒤에 띄어쓰기 1칸이 자동 적용



# 2-5 주석

# '#' 기호를 붙이면 그 문장이 주석 처리됨

# 한번에 여러 문장을 주석 처리 하고 싶으면 해당 문장들 드래그 후 Ctrl+/
# 한번에 여러 문장의 주석을 해제 하고 싶을 때도 해당 문장들 드래그 후 Ctrl+/
# 이어져 있는 문장을 주석처리 하고 싶으면 ''' 이어진문장 ''' 으로 표시

'''이렇게 하면 여러 문장이 
   한번에 주석 처리 됩니다'''




# Quiz 1. 변수를 이용해서 다음 문장을 출력하세요

# 변수명
# : Station

# 변수값
# : "사당", "신도림", "인천공항" 순대로 입력

# 출력 문장
# : XX행 열차가 들어오고 있습니다.




Station = "사당"
print(Station + "행 열차가 들어오고 있습니다.")

Station = "신도림"
print(Station, "행 열차가 들어오고")

Station = "인천공항"
print(Station + "행 열차가 들어오고 있습니다")

