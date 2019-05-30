def sigma0(n,a):
    value = 0
    while n > 0:
        if a <= n:
            value += n
            n = n-1
    return value

def sigma1(n,a):
    value = 0
    if n>=a:
        for x in range(n,a-1,-1):
            value += x
    return value

def sigma2(n,a):
    if n >= a:
        return n + sigma2(n-1,a)
    else :
        return 0

def sigma3(n,a):
    def loop(n,x):
        if n>=a:
            return loop(n-1,x+n)
        else:
            return x
    return loop(n,0)
