try:
    filename = input("열고자 하는 파일명을 입력하세요 >>> ")
    file = open(f'./section17/{filename}', 'rt')
    # file = open(f'{filename}', 'rt')
except:
    print(f"{filename} 파일이 존재하지 않습니다. ")
else:
    buffer = file.read()
    print(buffer)
    file.close()
finally:
    print("프로그램을 종료합니다.")