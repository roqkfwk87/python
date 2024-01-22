import time

class Sample:
    def __del__(self):
        print("인스턴스가 소멸됩니다.")

sample = Sample()
time.sleep(3)
del sample
input()