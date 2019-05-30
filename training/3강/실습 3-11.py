def rsmult(m,n):

    if n<=0:
        return 0

    a = 0

    while n>1:
        if n % 2 != 0:
            m, n, a= 2*m, n//2, m+a
        else:
            m, n= 2*m, n//2
    return m+a

print(rsmult(57, 0))
