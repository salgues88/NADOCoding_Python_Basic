# 10-2 에러 발생시키기

try:
    print("한자리 숫자 나누기 전용 게산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >= 10 or num2 >= 10:
        raise ValueError                                            # raise : 필요에 의해 일부러 에러를 발생시키는 방법
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:                                                  # ValueError : 파이썬에서 직접 제공하고 있는 에러
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자를 입력하세요")


###############################################################


# 10-3 사용자 정의 예외처리


# [메세지 없이 사용자 정의 예외 처리 하는 방법]
# class BigNumberError(Exception):                        # class 사용자변수(Exeption):\pass 로 사용자 정의 예외처리 가능
#     pass

# try:
#     print("한자리 숫자 나누기 전용 게산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요."))
#     num2 = int(input("두 번째 숫자를 입력하세요."))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:                                                  # ValueError : 파이썬에서 직접 제공하고 있는 에러
#     print("잘못된 값을 입력하셨습니다. 한 자리 숫자를 입력하세요")
# except BigNumberError:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요")







# [메세지 추가해서 사용자 정의 예외 처리 하는 방법]
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한자리 숫자 나누기 전용 게산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # BigNumberError 발생 시 해당 메세지가 출력됨
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:                                                  # ValueError : 파이썬에서 직접 제공하고 있는 에러
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자를 입력하세요")
except BigNumberError as err:                                       # BigNumberError as err 기능으로 지정한 메세지 출력가능
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요")
    print(err)