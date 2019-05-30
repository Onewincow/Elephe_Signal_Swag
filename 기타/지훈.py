def SearchWidestGap(s) :
    t = 0
    if len(s) == 0 :
        return (0,-1)
    elif len(s) == 1 :
        return (0,0)
    else :
        for x in range(len(s)-2) :
            a = s[x+1] - s[x]
            b = s[x+2] - s[x+1]
            if a >= b :
                if t < a:
                    k = x
                    t = a
            else:
                if t < b:
                    k = x+1
                    t = b
        return (t,k)
