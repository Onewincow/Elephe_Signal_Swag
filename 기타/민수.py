
def front_ok(front):
    year=front[0:2]
    month=front[2:4]
    day=front[4:6]
    if int(year)%4!=0:
            if (month== '02') and ('00'<day<'29'):
               return True
            if (month== '01' or '03' or '05' or '07' or '08' or '10' or '12') and ('00'<day<'32'):
                return True
            if (month== '04' or '06' or '09' or '11') and ('00'<day<'31'):
                return True
            else :
                return False
    if int(year)%4==0 :
            if (month=='02') and ('00'<day<'30'):
                return True
            if (month== '01' or '03' or '05' or '07' or '08' or '10' or '12') and ('00'<day<'32') :
                return True
            if (month== '04' or '06' or '09' or '11') and '00'<day<'31' :
                return True
            else:
                return False
def back_ok(s):
    a=s[0:1]
    b=s[1:2]
    c=s[2:3]
    d=s[3:4]
    e=s[4:5]
    f=s[5:6]
    g=s[7:8]
    h=s[8:9]
    i=s[9:10]
    j=s[10:11]
    k=s[11:12]
    l=s[12:13]
    m=s[13:]
    if m ==11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11) :
        return True
def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)

print(isRRN('000131-3020216'))
