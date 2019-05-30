# -*- coding: utf-8 -*-

# 순열 permutation
# assume: n > 0, k > 0, n >= k
# 양수 인수만 제대로 처리하면 된다.
# 즉, 인수가 양수인지는 함수 호출하기 전에 이미 확인했다고 가정한다.
# 그리고  n < k 인 경우에는 0을 내주도록 해야 한다.

def permutation(n,k):
    if n < k:
        return 0
    elif k > 0:
        return n * permutation(n-1,k-1)
    else:
        return 1

def permutation(n,k):

    if n < k:
        return 0

    def loop(n,k,p):
        if k > 0 :
            return loop (n-1,k-1,n*p)
        else:
            return p
    return loop(n,k,1)

def permutation(n,k):

    if n < k:
        return 0

    p=1
    while k>0:
        n, k, p= n-1, k-1, n*p

    return p

print(permutation(1,1))
print(permutation(2,1))
print(permutation(2,2))
print(permutation(3,1))
print(permutation(3,2))
print(permutation(3,3))
print(permutation(4,1))
print(permutation(4,2))
print(permutation(4,3))
print(permutation(4,4))
print(permutation(4,5))
