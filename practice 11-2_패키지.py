# 11-2 패키지


# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

# import로 외부에서 생성한 패키지를 불러올 때
import travel.thailand                              # import를 할 때 외부파일.xx에서 xx는 모듈이나 패키지만 올 수 있음
trip_to = travel.thailand.ThailandPackage()         # import에서 외부 class는 바로 불러올 수 없고 왼쪽 방식대로 사용해야함
trip_to.detail()



# from xxx import * 로 외부에서 생성한 패키지를 불러올 때
from travel.thailand import ThailandPackage         # from~ 으로 불러올 땐 ThailandPackage를 바로 불러오기 가능
trip_to = ThailandPackage()                         # from~ 에서는 파일이름 생략, 파일 내 class 이름만으로 불러오기
trip_to.detail()



# from~ 다른 방식으로 적용 케이스
from travel import vietnam
trip_to = vietnam.VietnamPackage()                  # 위에서 travel만 호출해서 여기선 vietnam.VietnamPackage()로 작성해야 함
trip_to.detail()

print("\n")




# 추가설명 : import 모듈 vs from 모듈 import 메소드 / 변수 차이

### 1) import 모듈→ 해당 모듈 전체를 가져옴, 사용하려면 항상 '모듈명.메소드' 와 같이 모듈명을 앞에 붙여주어야 한다.

### 2) from 모듈 import 메소드 / 변수 → 해당 모듈 내에 있는 특정 메소드나 모듈 내 정의된 변수를 가져옴,
###    가져온 메소드나 변수를 앞에 모듈명을 붙이지 않고 그대로 사용할 수 있음 (다만, 이름이 같은 변수나 메소드가 존재할 경우 대체됨)

### 3) from 모듈 import * 이라고 하면 import 모듈과 동일하다. (사용 시 모듈명 붙이는 것 빼고)






# [테크보이 워니 설명] https://www.youtube.com/watch?v=M6kQTpIqpLs&ab_channel=TeccboiWonie

# 파이썬 1시간 강의에서 배운 것 정리

# 개발환경 설정 (replit.com) / 변수 / 타입 / 조건문 / 함수 / 반복문 
# / 리스트 / 튜플 / 딕셔너리 / 클래스 / 오브젝트 / 패키지 / 모듈



# 파이썬 1시간 강의를 통해 배운것을 이용한 실생활 예제



# 예제1. 코드를 써서 핸드폰에 문자 보내기



# 이걸 하기 위해 알아야 할 개념 2가지 (1) 라이브러리, (2) API

# 라이브러리 == 다른 개발자가 자기 패키지를 공개해 놓은 것

# API : 서비스 개발자가 개발자들이 코드를 통해서 데이터를 가져갈 수 있도록 만들어 놓은 길 같은 것

# 예를 들어 날씨 정보를 가져오고 싶으면 (1) 기상청 홈피에서 날씨정보 보기, (2) 기상청 API를 써서 코드를 이용해서 정보 가져오기



# https://www.twilio.com/ 사이트 접속 -> (중간 설명은 유튜브 영상보고 파악하기) (패스워드 14자리...)

# twilio 접속 후 trial phone number : +19293251597

# twilio account SID : AC18fe3d8b8fdb34b4e8b88539dbb06286       (xx가 인식하는 ID)

# twilio auth token : de1622af30a9a1b18f3e1e5764046a17          (xx가 인식하는 PW)










