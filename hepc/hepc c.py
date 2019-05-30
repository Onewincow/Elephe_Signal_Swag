x = int(input())
memo = [[]] * (x+1)
for n in range(x+1):
    memo[n] = n//1
    if n // 2 > 0 and n//7 == 0 and n//5 ==0:
        a= n//2
        for b in range(a,0,-1):
            if memo[n] == []:
                memo[n] = min(memo[n],b + memo[n-(2*b)])
    if n // 5 > 0 and n//7 == 0:
        a= n//5
        for b in range(a,0,-1):
            if memo[n] == []:
                memo[n] = min(memo[n],b+memo[n-(5*b)])
    if n // 7 > 0 :
        a = n//7
        for b in range(a,0,-1):
            if memo[n] == []:
                memo[n] = min(memo[n],b+memo[n-(7*b)])
print(memo[x])
