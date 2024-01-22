s = "best of best"
print(s.find('b')) # 0 (인덱스 위치)
print(s.find('a')) # 없는 문자는 -1이 출력됨
print(s.find('o')) # 5

print(s.find('b', 5)) # 8
print(s.rfind('b')) # 8 (오른쪽부터 찾고, 찾은번호의 인덱스번호)