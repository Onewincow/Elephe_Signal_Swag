# -*- coding: utf-8 -*-

# 주민번호 앞자리
def front_ok(front):
    year = front[:2]
    month = front[2:4]
    day = front[4:]
    if month <'01' or month > '12':
        return False
    elif (month == '01' or '03' or '05' or '07' or '08' or '10' or '12') and (day < '01' or day > '31'):
        return False
    elif (month == '04' or '06' or '09' or '11') and (day < '01' and day > '30') :
        return False
    elif month == '02':
        if int(year)%4==0 and (day < '01' or day > '29'):
            return False
        elif int(year)%4!=0 and (day < '01' or day > '28'):
            return False
        else:
            return True
    else:
        return True

print(front_ok('990367'))

#주민번호 뒷자리
def back_ok(s):
    m = int(s[13])
    m == 11 - ((2*int(s[0])+3*int(s[1])+4*int(s[2])+5*int(s[3])+6*int(s[4])+7*int(s[5])+8*int(s[7])+9*int(s[8])+2*int(s[9])+3*int(s[10])+4*int(s[11])+5*int(s[12]) % 11))
    if (1<= m <=9) and (m == int(s[13])) :
        return True
    elif (10 <= m <= 11) and (m== int(s[13]) + 10):
        return True
    else:
        return False

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)
