n=int(input())
m=int(input())
if n == 1:
    print(1)
else:
    m=m-n
    b=1
    for a in range(1,n):
        b *= m+n-a
    for c in range(1,n):
        b //= c
    print(b)
