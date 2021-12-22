# 7-1 함수


# [테크보이 워니 설명]

# a = 1
# b = 2
# c = a + b

def dsum(a, b):
  result = a + b
  return result                                                     # return을 해야 계산된 값이 함수 외부로 나감

d = dsum(2, 4)
print(d)

print("\n")




# (나도코딩은 구두 설명만 하고 넘어감)




#######################################################################




#7-2 전달값과 반환값

# [나도코딩 설명] https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9

def open_account():                                                 # 함수 적을 때 변수 뒤에 내용 없으면 () 표시하기
    print("새로운 계좌가 생성되었습니다.")                            # 함수는 정의만 하는거지, 호출하기 전까지는 실행 X

open_account()                                                      # 함수를 호출하니 print가 실행됨

print()
print("[입금/출금 케이스 예제]")

def deposit(balance, money):                                        # 입금
    print("입금이 완료되었습니다. 잔액은 {0}입니다.".format(balance + money))
    return balance + money                                          # 잔고 + 입금액을 반환해줌

def withdraw(balance, money):                                       # 출금
    if balance >= money:                                            # 잔고가 출금보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0} 입니다.".format(balance - money))
        return balance - money
    
    elif balance <= money:
        print("잔고가 부족합니다. 잔액은 {0} 입니다.".format(balance))
        return balance


balance = 0                                                         # 잔액
balance = deposit(balance, 1000)                                    # 함수를 호출하니 함수 내 print 값이 출력됨
print(balance)                                                      # 현재 잔고가 표시됨

balance = withdraw(balance, 2000)                                   # balance = 1000, 출금 = 2000 -> 잔고 부족
balance = withdraw(balance, 500)



print("[커미션 추가 케이스 예제]")

def withdraw_night(balance, money):                                 # 저녁에 출금
    commission = 100                                                # 수수료 = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))



