'''
1. Song 클래스 정의, 인스턴스 변수(노래제목, 장르)
2. Singer 클래스 정의, 인스턴스 변수(가수 이름, 대표곡) 
3. 출력결과
가수이름 : 김동률
노래제목 : 취중진담(발라드)
'''

class Song:
    def set_song(self, title, gender):
        self.title = title
        self.gender = gender

    def print_song(self):
        print(f"노래제목 : {self.title}({self.gender})")

class Singer:
    def set_singer(self, name):
        self.name = name

    def hit_song(self, Song):
        self.song = song
        
    def print_singer(self):
        print(f"가수이름 : {self.name}")
        # print(f"노래제목 : {self.song.title}({self.song.gender})")
        song.print_song()

song = Song()
song.set_song("취중진담", "발라드")
# print(song.title)
# print(song.gender)

singer = Singer()
singer.set_singer("김동률")
singer.hit_song(song)

singer.print_singer()