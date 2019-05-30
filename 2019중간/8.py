# -*- coding: utf-8 -*-

### 8. 12시간 시계를 24시간 시계로 변환
def clock12to24(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    amORpm = minuteplus[-2:]
    if len(hour) == 1:
        hour = '0'+hour
    if amORpm == 'pm':
        if hour != '12':
            hour = str(int(hour)+12)
    else: # amORpm == 'am'
        if hour == '12':
            hour = '00'
    return hour + colon + minute

print(clock12to24("12:00am")) # 00:00
print(clock12to24("12:05am")) # 00:05
print(clock12to24("1:30am")) # 01:30
print(clock12to24("3:05am")) # 03:05
print(clock12to24("12:00pm")) # 12:00
print(clock12to24("12:08pm")) # 12:08
print(clock12to24("3:50pm")) # 15:50
print(clock12to24("9:12pm")) # 21:12
print(clock12to24("11:59pm")) # 23:59
