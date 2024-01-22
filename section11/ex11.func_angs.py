"선언"
a = 0 
"정의"

# 함수 정의 => def 
def show(*args): # argument : 인수 
    for item in args :
        print(item, end= ' ') 
    print("!")


show("python", "is", "Best")


# a = show("python is Best")
# print("a : ", a)