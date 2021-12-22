# 11-7 내장함수

# # input : 사용자 입력을 받는 내장함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))



# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 동시에 가지고 있는지 표시하는 내장함수

print("\n")
print(dir())                                                # random 외장함수 import 하기 전

print("\n")
import random                                               # 외장함수 불러오기
print(dir())                                                # random 외장함수 import 후, dir 함수값 + random

print("\n")
import pickle
print(dir())                                                # dir 함수 값 내에 pickle, random 추가됨

print("\n")
# random.randint                                            # dir은 random 뒤에 점(.)을 찍었을 때 나오는 내용을 모두 표시함
print(dir(random))                                          # 랜덤 함수 내의 변수, 함수값을 모두 표시


print("\n")
lst = [0, 1, 2]
print(dir(lst))                                             # lst 함수에서 사용가능한 모든 항목을 표시


print("\n")
name = "jim"                                                # name 함수에서 사용가능한 모든 항목을 표시
print(dir(name))


# 구글에서 'list of python builtins' 검색 -> 내장, 외장함수에서 사용 가능한 built-in function(=내장함수) 을 보여줌

# https://docs.python.org/3/library/functions.html