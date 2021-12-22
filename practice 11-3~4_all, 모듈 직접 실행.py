# 11-3 all

from travel import *                                # ~~ * : travel(패키지)내의 모든 것을 불러오겠다는 뜻
trip_to = vietnam.VietnamPackage() 
trip_to.detail()

# NameError : name 'vietnam' is not defined  (이름에러 : 베트남이 설정되지 않았음)
# -> 패키지 내의 파일들 중 공개를 원하는 것 / 원하지 않는 것을 구분해야 함
# -> 패키지 폴더 내에 만든 __init__에 공개 여부를 설정할 필요가 있음
# -> __init__.py 파일 내에  '__all__ = ["vietnam"]'  입력 필요      (베트남 파일 공개 허용)


# 정상적인 코드에 붉은줄 표시됨
# File -> Preference -> Settings -> linting 검색 -> Python Linting:Enabled 체크 해제



# 현재 __init__.py 파일에 vietnam만 설정되어 있을 때 thailand 불러오기
trip_to = thailand.ThailandPackage() 
trip_to.detail()

# 에러 : thailand가 정의되지 않음 (∵ __init__에 베트남만 적었으니 태국은 불러오기 불가)
# -> __all__ = ["vietnam", "thailand"] 에 태국 추가                 (태국 파일 공개 허용)
# -> 실행하면 인식 잘 됨




################################################################################




# 11-4 모듈 직접 실행 : 모듈이 모듈 내부에서 실행되는지, 모듈 외부에서 실행되는지를 표시하기 위한 구문 추가 방법

# 모듈을 직접 실행하고, 외부에서 호출되는걸 표시하기 위해 travel 폴더 (패키지) 내의 thailand.py로 이동하여 구문 작성 (if ~~)

# tahiland.py에 모듈 직접 실행을 위한 구문 추가 후 실행
# -> ~~외부에서 호출됨~~ 이라고 표시되는걸 확인