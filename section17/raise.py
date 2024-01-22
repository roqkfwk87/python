'''
사용자로부터 나이 입력받기!
0~ : 양수
-100
raise 명령어 고의(의도적으로)로 에러 발생
'''

age = int(input("나이를 입력하세요 >>> "))

try:
    if age < 0:
        raise Exception("음수 나이는 입력할 수 없습니다. ")
    print(f"당신의 나이는 {age}입니다.")
except Exception as e:
    print(e)