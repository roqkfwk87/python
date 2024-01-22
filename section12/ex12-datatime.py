import datetime # 날짜, 시간 다름

present = datetime.datetime.now()
print(present)

birthday = datetime.date(1950, 1, 1)
print(birthday)

wake =  datetime.time(10, 48, 0)
print(wake) # 10:48:00

print(present.year)
print(present.month)
print(present.day)
print(present.minute)
print(present.second)\

yesterday = present - datetime.timedelta(days=1) # 1일
print(yesterday)

date1 = datetime.date(2023, 12, 10)
date2 = datetime.date(2023, 12, 11)
tomorrow_seconds = (date1 - date2).total_seconds()
print(tomorrow_seconds) # 86400.0