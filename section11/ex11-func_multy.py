# 다중 반환 : 여러개 변환값
#변환값 반드시 1개 !!!
def calculator(*args):
    return sum(args), max(args), min(args) #튜플

a, b, c = calculator(1,2,3,4,5) #(15, 5, 1)
print("합계 : ", a)
print("최대값 : ", b)
print("최소값 : ", c)
print("튜플: ", calculator(1,2,3,4,5)  )