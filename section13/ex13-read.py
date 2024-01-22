file = open('./section13/sample.txt', 'r') 
# read
# readline()
# readlines()

# str = file.read() # 글자 수 만큼 가져옴
# print(str)

# while True:
#     str = file.readline() 
#     if str == '':
#         break
#     print(str, end='')

line_list = file.readlines() 
print(line_list)