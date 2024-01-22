# 생성자, 소멸자
class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        print(f"{name} is born")
        Person.count += 1
        # print(Person.count)

    def __del__(self):
        print(f"{self.name} is dead")
        Person.count -= 1
        
    @classmethod
    def get_count(cls):
        return cls.count
    
man = Person("james")
woman = Person("emily")

print(f"전체 인구수: {Person.get_count()}")

del man 

print(f"전체 인구수: {Person.get_count()}")
input()