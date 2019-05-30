# -*- coding: utf-8 -*-

### 7. 12시간 시계 형식 확인
def validClock12(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    amORpm = minuteplus[-2:]
    return len(minuteplus) == 4 and '00' <= minuteplus < '60' and ((len(hour) == 2 and int(hour[0]) != 0) or (len(hour)==1 and int(hour[0]) != 0))


print(validClock12("1:30am")) # True
print(validClock12("9:12pm")) # True
print(validClock12("3:05am")) # True
print(validClock12("10:14pm")) # True
print(validClock12("11:59pm")) # True
print(validClock12("12:00am")) # True
print(validClock12("12:00pm")) # True
print(validClock12("0:15am")) # False

print(validClock12("09:18pm")) # False
print(validClock12("3:5am")) # False
print(validClock12("00:00pm")) # False

print(validClock12("5:60am")) # False
