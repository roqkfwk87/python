# 1. Book 클래스 정의
# 2. 메서드 정의
    # - set_info() # 변수명 : title, author
    # print_info() 정의
# 3. book1, book2 인스턴스
# 4. book_list 저장
# 5. 실행결과
# 책 제목 : 파이썬
# 책 저자 : 민경태
# 책 제목 : 어린왕자
# 책 저자 : 생텍쥐페리

class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"책 제목 : {self.title}") 
        print(f"책 저자 : {self.author}") 

book1 = Book()
book2 = Book()
book1.set_info("파이썬", "민경태")
book2.set_info("어린왕자", "생텍쥐페리")

book_list = [book1, book2]

for book in book_list:
    book.print_info()
