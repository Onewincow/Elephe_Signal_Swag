def findXth(X):
    if X == 1:
        return 1/1
    n = 1
    m = 0
    while d
        m += 1
        x -= 1
        n += 1

def reflica(x,a):
    n=1
    while((2*a+(n-1)*4)/2*n<x):
        n=n+1
    return min(4*(n-1)+a-((2*a+(n-1)*4)/2*n-x),(((2*a+(n-1)*4)/2*n-x))+1)
X=int(input())
print(str(int(reflica(X,1)))+"/"+str(int(reflica(X,3))))
