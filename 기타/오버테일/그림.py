a=int(input())
for i in range(0,a):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,a-i):
        print("*",end="")
    print("")

 a=int(input())
for i in range(0,2*a-1):
    for j in range(0,a-1-abs(a-1-i)):
        print(" ",end="")
    for k in range(0,2*abs(a-1-i)+1):
        print("*",end="")
    print("")

def nCk(n,k):
    if(n==0 or k==0 or n==k):
        return 1
    else:
        return n*nCk(n-1,k-1)//k

a=int(input())
for i in range(0,a):
    for k in range(0,a-i-1):
        print("\t",end="")
    for j in range(0,i+1):
        print("\t"+str(nCk(i,j)),end="\t")
    print("")
