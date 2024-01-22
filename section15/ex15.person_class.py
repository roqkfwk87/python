class Person: # 파스칼 케이스
    # 인스턴스 메서드
    def who_am_i(self, name, age, tel, address):
        # 인스턴스 변수
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

kim1 = Person()
kim2 = Person()
kim3 = Person()

kim1.who_am_i("김일남", 99, "010-1111-1111", "부산")
kim2.who_am_i("김이남", 98, "010-2222-2222", "서울")
kim3.who_am_i("김삼남", 97, "010-3333-3333", "울산")

print(kim1.name, kim1.tel)
print(kim2.name, kim2.tel)
print(kim3.name, kim3.tel)

# 재사용서, 유지보수성