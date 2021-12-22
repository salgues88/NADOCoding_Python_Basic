# 11-8 외장함수 : 외부에서 직접 import 해서 사용하는 함수

# 구글 -> list of python module

# 외장함수 예시

# # glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))                                    # 확장자가 .py인 모든 파일



# # os : 운영체제에서 기본 제공하는 기능
# import os
# print(os.getcwd())                                          # 현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")                        # (두번 이상 실행 시 이미 폴더가 존재해서 해당 문구 출력)
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")                   # (기존 폴더가 존재하면 삭제하는 기능)
# else:
#     os.makedirs(folder)                                     # 폴더 생성 (처음 실행 시 폴더가 없으니 폴더 생성됨)
#     print(folder, "폴더를 생성하였습니다.")                 

# print(os.listdir())                                         # 디렉토리 내 모든 파일명 불러오기




# time : 시간 관련 함수
# import time
# print(time.localtime())                                         
# print(time.strftime("%y-%m-%d %H:%M:%S"))                     # 21-07-08 15:37:49   



# datetime
import datetime
print("오늘 날짜는", datetime.date.today())



# timedelta : 두 날짜 사이의 간격 표시
today = datetime.date.today()                                   # 오늘 날짜 저장
td = datetime.timedelta(days=100)                               # 100일 저장
print("우리가 만난 100일은", today + td)                         # 오늘부터 100일 후