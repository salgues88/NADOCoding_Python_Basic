# 8-5 with : with를 활용하면 2문장으로 쓰기, 불러오기 가능, 사용한 파일을 별도로 close 해 줄 필요 없음


# <with를 이용하여 pickle 파일을 간편하게 불러오기>
import pickle

with open("profile.pickle", "rb") as profile_file:      # profile.pickle 이라는 파일을 불러와서 profile_file에 저장
    print(pickle.load(profile_file))                    # profile_file에 저장된 값을 불러와서 출력 (따로 close 해줄 필요 없음)



# <일반 파일을 with를 이용하여 작성하고(쓰기), 변수에 내용 저장하기>
# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")    # 2줄로 파일 생성 가능. 따로 close 해줄 필요 없음



# <일반 파일을 with를 이용하여 불러오기>
with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read())




# Quiz7. 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.

# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 형태로 만드시오




# 해답 1 (나도코딩)

dept = "생산자동화"

name = "이창준"

w_summary = "나도코딩 파이썬 기초 공부"


for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
        report_file.write("- {0}주차 주간보고 -".format(i))
        report_file.write("\n부서 : {0}".format(dept))
        report_file.write("\n이름 : {0}".format(name))
        report_file.write("\n업무 요약 : {0}".format(w_summary))





# 해답 2 (나) (실패)

#dept = "생산자동화"

#name = "이창준"  

#w_summary = "나도코딩 파이썬 기초 공부"

#for i in range(1, 51):
#    with open("{0}주차.txt".format(i), "w", encoding = "utf8") as report_file:
#        report_file.write("- {0}주차 주간보고 -".format(i), end = "")
#        report_file.write("부서 : {0}".format(dept), end = "")
#        report_file.write("이름 : {0}".format(name), end = "")
#        report_file.write("업무 요약 : {0}".format(w_summary))




# with opne("{0}")

# for 