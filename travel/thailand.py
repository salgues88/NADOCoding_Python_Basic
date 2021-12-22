# 11-1 모듈 
class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


# 11-4 모듈 직접 실행을 위한 구문 추가
if __name__ == "__main__":
    print("--Thailand 모듈을 직접 실행--")
    print("--이 문장은 모듈을 직접 실행할 때만 실행됨--")
    trip_to = ThailandPackage()
    trip_to.detail
else:
    print("--Thailand 파일 외부에서 호출됨--")