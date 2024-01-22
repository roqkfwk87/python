class Korean:
    country = "한국"

    # 정적메서드
    @staticmethod
    def trip(country):
        if Korean.country == country:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")

# print(Korean.country)
Korean.trip("한국")
Korean.trip("미국")
k = Korean()
k.trip("한국")
k.trip("미국")