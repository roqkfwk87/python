class Korean:
    country = "한국"

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

Kim1 = Korean("김일남", "M")
Kim2 = Korean("김일여", "W")

# print(f"{Kim1.name}씨는 성별이 {Kim1.gender} 입니다. 국적은 {Kim1.country}입니다. ")
print(f"{Kim1.name}씨는 성별이 {Kim1.gender} 입니다. 국적은 {Korean.country}입니다. ")
print(f"{Kim2.name}씨는 성별이 {Kim2.gender} 입니다. 국적은 {Kim2.country}입니다. ")