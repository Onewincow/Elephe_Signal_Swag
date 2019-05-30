# -*- coding: utf-8 -*-
def is_valid_date(year,month,day):
    return year > 0 and 1 <= month <= 12 and \
           (month in [1,3,5,7,8,10,12] and 1 <= day <= 31 or
            month in [4,6,9,11] and 1 <= day <= 30 or
            is_leap_year(year) and 1 <= day <= 29 or
            1 <= day <= 28)

def get_valid_date_6(s):
    if '0'< s[0:2] < '18':
        return is_valid_date(int('20' + s[0:2]), int(s[2:4]), int(s[4:6]))
    else:
        return is_valid_date(year, month, day = int('19' + s[0:2]), int(s[2:4]), int(s[4:6]))
    if is_valid_date(year,month,day):
        return (year,month,day)
    else:
        return None


# 입력 테스트 케이스
print(get_valid_date_6(160425)) # => (2016, 4, 25)
160431 # => None
160229 # => (2016, 2, 29)
170229 # => None
450815 # => (1945, 8, 15)
