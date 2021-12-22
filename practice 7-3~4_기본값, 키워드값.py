# 7-3 기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))                               # \t : 탭, \ + 엔터 : 줄바꿈 (하나의 문장으로 처리됨)

# profile("유재석", 30, "파이썬")
# profile("조세호", 25, "자바")



# 같은 학교 같은 학년, 같은 반, 같은 수업 -> 중복되는 부분을 기본값으로 표현 가능

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))                              

profile("유재석")
profile("조세호")



#################################################################################################################


# 7-4 키워드값                                                        

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=30)
profile(main_lang="자바", name="조세호", age=29)