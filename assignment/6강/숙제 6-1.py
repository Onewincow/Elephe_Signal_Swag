def minsteps1(n):
    memo = [0] * (n + 1)
    def loop(n):
        if n > 1:
            if memo[n] != 0:
                return memo[n]
            else:
                memo[n] = 1 + loop(n - 1)
                if n % 2 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 2))
                if n % 3 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 3))
                return memo[n]
        else:
            return 0
    return loop(n)


def minsteps (n):
    memo = [0] * (n + 1)
    for x in range(2,n+1):
        memo[x] = memo[x-1] + 1
        if x % 2 == 0:
            memo[x] = min(memo[x],memo[x//2]+1)
        if x % 3 == 0:
            memo [x] = min(memo[x],memo[x//3]+1)
    return memo[n]

print(minsteps(10))
