# -*- coding: utf-8 -*-

### 9. 종료시간 계산하기

def minutesAfter(time, passedMinute):
    (hour,_,minute) = time.partition(":")
    passedHour = passedMinute // 60
    passedMinute = passedMinute % 60
    hour = int(hour) + passedHour
    minute = int(minute) + passedMinute
    count=0
    while minute >= 60:
        minute = minute - 60
        count = count + 1
    hour += count
    return str(hour) + ":" + str(minute)

print(minutesAfter("3:34",100)) # 5:14
print(minutesAfter("11:45",20)) # 12:5
print(minutesAfter("9:59",1)) # 10:0
print(minutesAfter("123:10",200)) # 126:30
