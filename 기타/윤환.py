def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)

def front_ok(front):
    year = front[0:2]
    month = front[2:4]
    day = front[4:6]
    if int(year) % 4 == 0:
        if month == '02':
            if '0' < day < '30':
                return True
            else:
                return False
        elif month == '01' or month =='03' or month =='05' or month =='07' or month =='08' or month =='10' or month =='12':
            if '0' < day < '32':
                return True
            else:
                return False
        elif month == '04'or month == '06' or month == '09' or month == '11':
            if '0' < day < '31':
                return True
            else:
                return False
        else:
            return False
    elif int(year) % 4 != 0:
        if month == '02':
            if '0' < day < '29':
                return True
            else:
                return False
        elif month == '01' or month =='03' or month =='05' or month =='07' or month =='08' or month =='10' or month =='12':
            if '0' < day < '32':
                return True
            else:
                return False
        elif month == '04'or month == '06' or month == '09' or month == '11':
            if '0' < day < '31':
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def back_ok(s):
    a=int(s[0:1])
    b=int(s[1:2])
    c=int(s[2:3])
    d=int(s[3:4])
    e=int(s[4:5])
    f=int(s[5:6])
    g=int(s[7:8])
    h=int(s[8:9])
    i=int(s[9:10])
    j=int(s[10:11])
    k=int(s[11:12])
    l=int(s[12:13])
    m=int(s[13:])
    if m == 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11):
        return True
    else:
        return False

print(front_ok('123456'))
