def isleapyear(year):
    if year >= 0:
        if year<100:
            if year%4 == 0:
                return True
            else:
                return False
        else:
            if year%100==0:
                if year%400!=0:
                    return False
                else:    
                    return True

            elif year % 4 ==0:
                return True

            else:
                return False
    if year < 0:
        return None
