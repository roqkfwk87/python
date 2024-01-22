
while True:
    a = int(input("제수를 입력하세요 >>> "))
    b = int(input("피제수를 입력하세요 >>> "))

    try:
        print(f"{a} / {b} =  {a/b}")
    except:
        print("0으로는 나눌수 없습니다.")