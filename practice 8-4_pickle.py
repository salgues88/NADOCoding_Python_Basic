# 8-4 pickle : 어떤 정보를 pickle에 저장한 후 (binary 형태), 다시 불러 올 수 있는 유용한 라이브러리
#              텍스트 외 자료형태를 파일로 저장하기 위해 pickle이라는 모듈 사용

# <pickle 파일 생성>
import pickle                                           # pickle 불러오기 (random 불러오는 것과 유사)

# profile_file = open("profile.pickle", "wb")             # wb : write binary (pickle을 쓰기 위해서는 항상 binary 타입으로 정의해야 함)
#                                                         # (pickle에서는 따로 encoding을 설정할 필요 X)
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)                      # pickle에 있는 정보를 file에 저장
# profile_file.close()



# <pickle 파일 불러오기>

profile_file = open("profile.pickle", "rb")             # rb : read binary
profile = pickle.load(profile_file)                     # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()


