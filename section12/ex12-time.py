import time # 시간을 다루는 모듈

print(time.time()) # 현재 시간을 초로 리턴함 (소주점 이하는 마이크로초) 밀릴초(1/1000), 마이크로초(1.1000000), 1970-1-1 00:00:00 리눅스
print(time.ctime(1702169985.5427718)) # Sun Dec 10 09:59:45 2023

# 2023-12-10 00:00:00
print(time.strftime('%Y-%m-%d %a %H:%M:%S')) # 2023-12-10 Sun 10:05:38

time.sleep(3) # 아래 코드의 실행을 1초간 중지
print(time.strftime('%Y/%m/%d %H:%M')) # 2023/12/10 10:06
