# 8-3 파일 입출력

# <파일 생성하기>

# score_file = open("score.txt", "w", encoding="utf8")               # w : write(쓰기), encoding="utf8" : 한글 인식이 되는 인코딩 방식
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()                                                 # 파일을 열었으면 항상 닫아줘야 함. 

# (위 까지 코드 작성 후 실행하면 score.txt 파일 생성됨)


# <파일 내용 추가하기>

# score_file = open("score.txt", "a", encoding="utf8")               # a : append(추가)  (기존 파일에 내용 추가)
# score_file.write("과학 : 80")                                       # 파일명.write(추가내용)
# score_file.write("\n코딩 : 100")                                    # 그대로 붙여넣으면 줄바꿈 X -> \n으로 줄바꿈


# <파일 전체내용 불러오기>

# score_file = open("score.txt", "r", encoding="utf8")               # r : read(읽기)
# print(score_file.read())                                           # 파일명.read() : 파일 내 모든 내용 불러오기


# <파일 1줄 씩 불러오기>

# score_file = open("score.txt", "r", encoding="utf8") 
# print(score_file.readline())                                       # 파일명.readline() : 파일 내 1줄 씩 불러오기, 1줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())                                       # (readline을 연속 사용 시에는 자동 줄바꿈 적용됨)
# print(score_file.readline(), end = "")                             # (end=""으로 바로 밑의 줄과 연결 (자동 줄바꿈 사라짐))
# print(score_file.readline())
# score_file.close()



# <다른 사람이 불러온 파일이 총 몇줄인 줄 모를 떄 반복문을 이용하여 불러오기>
# score_file = open("score.txt", "r", encoding="utf8") 
# while True:
#     line = score_file.readline()
#     if not line:                                                   # 반복문 탈출
#         break                                                      # 총 몇줄인줄 모를 떄는 반복문을 통해 모든 줄을 불러올 수 있음
#     print(line, end = "")
# score_file.close()


# <파일명.readlines 기능을 통해 list 형태로 저장>
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()                                      # list 형태로 저장
for line in lines:
    print(line, end = "")
score_file.close()