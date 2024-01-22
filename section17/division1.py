
while True:
    a = int(input("제수를 입력하세요 >>> "))
    b = int(input("피제수를 입력하세요 >>> "))

    if b != 0:
        print(f"{a} / {b} =  {a/b}")
    else:
        print("0으로는 나눌수 없습니다.")