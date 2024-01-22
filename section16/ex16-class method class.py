class Korean:
    country = "한국"

    @classmethod
    def trip(cls, country):
        if Korean.country == country:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")

# print(Korean.country)
Korean.trip("한국")
Korean.trip("미국")