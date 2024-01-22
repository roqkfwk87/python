# % 연산자
# result = 3000
# candy = 1000
# result = total - candy
# print('금액 : %d원', % result)

# %o
# print('십진수%d은 8진수 : %o' %(10, 10))
# print('%x' % 10)
# print('%.1f' % 10)
# print('%d' % 'python') #타입 에러
# print('hello%-10s!' % 'python')
name = 'kai'
print("내 이름은 %s입니다." % name)

height = 120.5
# print("내 키는 %fcm입니다." %height)
print("내 키는 %.3fcm입니다." %height)

weight = 23.55
print('내 몸무게는 %fkg입니다.' %weight)

# 구조 분해 할당
year, month, day = 2014, 8, 25 
print("내 생일은 %d년 %d월 %d일입니다." %(year, month, day))
