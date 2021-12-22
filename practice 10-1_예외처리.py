# 10-1 예외처리


# try:                                                                    # try: 내의 문장을 체크
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# # 출력문에 숫자 말고 문자를 입력하면 오류 발생함 (num1 = 6, num2 = 마) -> 이럴 때 예외처리를 활용함
# except ValueError:                                                      # 숫자 대신 문자가 들어가면 해당 코딩 발동
#     print("에러! 잘못된 값을 입력하셨습니다.")

# # 출력문에 num1 = 6, num = 0 일 때 -> 6/0 = 무한대 -> ZeroDivisionError 발생
# except ZeroDivisionError as err:                                        # as err : 출력문 값의 에러 표시를 출력으로 표시
#     print(err)




#

try:                                                                # try: 내의 문장을 체크
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))                           # 이 부분을 없애면 밑의 except: 가 발동됨 (∵ )
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# 출력문에 숫자 말고 문자를 입력하면 오류 발생함 (num1 = 6, num2 = 마) -> 이럴 때 예외처리를 활용함
except ValueError:                                                  # 숫자 대신 문자가 들어가면 해당 코딩 발동
    print("에러! 잘못된 값을 입력하셨습니다.")

# 출력문에 num1 = 6, num = 0 일 때 -> 6/0 = 무한대 -> ZeroDivisionError 발생
except ZeroDivisionError as err:                                    # as err : 출력문 값의 에러 표시를 출력으로 표시
    print(err)

# 위 오류 2 케이스를 제외한 발생하는 모든 오류의 예외 처리는 except: 를 사용하여 처리가능

# except:
#     print("오류가 발생하였습니다.")


# 발생하는 모든 오류 케이스에 대한 메세지를 받고 싶다면 except Exception as err: 로 출력문 에러 확인 가능
except Exception as err:
    print("오류가 발생했습니다")                                      # nums 리스트의 2번째 자리 부분 설정 X
    print(err)                                                       #  -> list index out of error