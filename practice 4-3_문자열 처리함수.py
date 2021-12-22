python = "Python is Amazing"

print(python.lower())                   # 변수.lower() : 문자열을 소문자로만 표시
print(python.upper())                   # 변수.upper() : 문자열을 대문자로만 표시

print(python[0].isupper())              # 변수[숫자].isupper : 몇번째 자리의 문자가 대문자인가? True or False (0부터 시작)

print(len(python))                      # len(변수) : 문자열 글자 총 개수를 숫자로 표시

print(python.replace("Python", "Java")) # 변수.replace("원래 문자열", "변경할 문자열")


index = python.index("n")               # 변수.index("특정 알파벳") 
print(index)                            # : 문장 내 특정 알파벳 여러개 중에서 1번째 특정 알파벳 위치 표시 (0부터 시작)

index = python.index("n", index + 1)    # 변수.index("특정 알파벳", index + 1) 
print(index)                            # : 문장 내 특정 알파벳 여러개 중에서 2번재 특정 알파벳 위치 표시 (0부터 시작)

print(python.find("n"))                 # 변수.find("특정 알파벳")  = 변수.index("특정 알파벳") 

#print(python.find("x"))                # 특정 알파벳 위치 찾을 때 없는 글자면 출력값에 -1 로 표시됨 (이후에 있는 내용을 이어서 출력함)
#print(python.index("x"))               # 특정 알파벳 위치 찾을 때 없는 글자면 출력값에 에러로 표시되면서 출력이 종료됨 (이후에 있는 내용은 출력 안 됨)

print(python.find("x"))                 
print("Hello World")                    

#print(python.index("x"))
print("Hi")                           


print(python.count("n"))                # 변수.count("특정 알파벳") : 특정 알파벳이 총 몇번 나오는지 숫자로 표시
