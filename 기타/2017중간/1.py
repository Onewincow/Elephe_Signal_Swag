# -*- coding: utf-8 -*-
#재귀함수
def trinum(n):
    if n >= 1:
        return n+trinum(n-1)
    else:
        return 0

print(trinum(1)) # 1
print(trinum(3)) # 6
print(trinum(6)) # 21
print(trinum(11)) # 66
print(trinum(0)) # 0
print(trinum(-3)) # 0

# 꼬리재귀함수
def trinumT(n):
    def loop(n,r):
        if n>=1:
            return loop(n-1, r+n)
        else:
            return r
    return loop(n,0)

# 테스트 케이스
print(trinumT(1)) # 1
print(trinumT(3)) # 6
print(trinumT(6)) # 21
print(trinumT(11)) # 66
print(trinumT(0)) # 0
print(trinumT(-3)) # 0

# while 문 함수
def trinumW(n):
    r=0
    while n>=1:
        n, r= n-1, r+n
    return r

# 테스트 케이스
print(trinumW(1)) # 1
print(trinumW(3)) # 6
print(trinumW(6)) # 21
print(trinumW(11)) # 66
print(trinumW(0)) # 0
print(trinumW(-3)) # 0
