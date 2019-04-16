def front_ok(front):
    year = front[0:2]
    month = front[2:4]
    day = front[4:6]
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
            if month == '02':
                if '0' < day < '30':
                    return True
                else:
                    return False
            elif month == '01' or '03' or '05' or  '07'or '08' or '10' or '12':
                if '0' < day < '32':
                    return True
                else:
                    return False
            elif month == '04' or '06' or '09' or '11':
                if '0' < day < '31':
                    return True
                else:
                    return False
        elif int(year) % 400 != 0:
            if month == '02':
                if '0'< day < '29':
                    return True
                else:
                    return False
            elif month == '01' or '03' or'05' or  '07'or '08' or '10' or '12':
                if '0' < day < '32':
                    return True
                else:
                    return False
            elif month == '04' or '06' or '09' or '11':
                if '0' < day < '31':
                    return True
                else:
                    return False
        elif int(year) % 100 != 0:
            if int(year) % 4 == 0:
                if month == '02':
                    if '0' < day <'30':
                        return True
                    else:
                        return False
                elif month == '01' or '03' or '05' or  '07'or '08' or '10' or '12':
                    if '0' < day < '32':
                        return True
                    else:
                        return False
                elif month == '04' or '06' or '09' or '11':
                    if '0' < day < '31':
                        return True
                    else:
                        return False
            elif int(year) % 4 != 0:
                if month == '02':
                    if '0'< day < '29':
                        return True
                    else:
                        return False
                elif month == '01' or '03' or '05' or  '07'or '08' or '10' or '12':
                    if '0' < day < '32':
                        return True
                    else:
                        return False
                elif month == '04' or '06' or '09' or '11':
                    if '0 '< day < '31':
                        return True
                    else:
                        return False
    else:
            return True

print(front_ok('981111'))
