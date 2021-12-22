

# def profile(name, age, main_lang1, main_lang2, main_lang3, main_lang4, main_lang5):
#     print("이름 : {0}\t나이 : {1}세".format(name, age), end = " ")         # end = " " : 줄바꿈없이 위아래를 이어서 출력
#     print(main_lang1, main_lang2, main_lang3, main_lang4, main_lang5)

# profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#")
# profile("조세호", 22, "Kotlan", "Swift", " ", " ", " ")



def profile(name, age, *language):                                          # *변수 : 가변인자용 변수
    print("이름 : {0}\t나이 : {1}세".format(name, age), end = " ")
    for lang in language:                                                   # for을 이용하여 순차적으로 표시
        print(lang, end = " ")                                              # 순차적으로 나오는 값들을 end로 연결
    print()

    
profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#", "프로그램 언어")
profile("조세호", 22, "Kotlan", "Swift", " ", " ", " ")
