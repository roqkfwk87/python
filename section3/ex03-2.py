# 함수에 넣는 값(인풋값) == "인수", "argument"
#print("hello", "python")
#print("hello", "python", sep="")
# print("hello", end="\n")
# print("python", end="\n")
# print("hello")
# print("python")
# print("hello", "python", end="!")
# print("hello", "python", sep=" ", end="!\n")
# print("hello", "python", sep=" ", end="!")

#file
fos = open('sample.py', mode='wt') #wt = write text

print ('print("Hello python")', file=fos)
import sys
fos = open('sample.py', 'w') #wt = write text

# print('print("Hello Python!")', file=sys.studout)
print('print("Hello Python!")', file=fos)

