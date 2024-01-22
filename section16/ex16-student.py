class Person:
    def __init__(self, name):
        self.name = name 

    def eat(self, food):
        print(f"{self.name}씨가 {food}을 먹습니다.")

# Kim1 = Person("김일남")
# Kim1.eat("밥")
# Kim2 = Person("김이남")
# Kim2.eat("밥")

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(f"{self.name}는 {self.school}에서 공부를 합니다. ")

Kim1 = Student("김일남", "코리아아이티아카데미")
Kim1.study()
Kim1.eat("밥")

Kim2 = Person("김이남")
Kim2.eat("밥")
print(isinstance(Kim1, Student))
print(isinstance(Kim1, Person))
print(isinstance(Kim2, Person))
print(isinstance(Kim2, Student))