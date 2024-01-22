class Service:
    def __init__(self, service):
        self.service = service
        print(f"{self.service} Service가 시작되었습니다.")

    def __del__(self):
        print(f"{self.service} Service가 종료되었습니다.")

s = Service("길 안내")
input()
del s 