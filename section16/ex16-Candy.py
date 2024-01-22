# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color

# satang = Candy()
# satang.set_info("동그라미", "노랑")
# print(satang.shape)
# print(satang.color)

class Candy:
    def __init__(self, shape, color): # __!던더스코어
        self.shape = shape
        self.color = color

satang = Candy("동그라미", "노랑")
print(satang.shape)
print(satang.color)