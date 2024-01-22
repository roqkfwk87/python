
try:
    a = int(input("제수를 입력하세요 >>> "))
    b = int(input("피제수를 입력하세요 >>> "))
    print(f"{a} / {b} =  {a/b}")

except ZeroDivisionError:
    print("0으로는 나눌수 없습니다.")

except ValueError:
    proint("정수만 입력할 수 있습니다.")
