# -*- coding: utf-8 -*-

# 덧셈만으로 제곱 계산
# 작성한 함수는 정수 인수에 대해서 제대로 작동하면 된다.
# 그런데 앞 문제와는 달리 음수 인수에 대해서도 제대로 작동해야 함을 명심하자.

def square(n):
    def loop(n):
        if n > 0:
            return 2 * n - 1 + loop (n-1)
        else:
            return 0
    return loop(abs(n)) # 음수를 처리하려면 이 부분을 손봐야 한다.

def square(n,o):
    def loop(n,o): # 꼬리 재귀
        if n > 0 :
            return (n-1, 2*n-1+o)
        else:
            return o
    return square(abs(n),0)

def square(n):
    if n<0:
        n = -1 * n
    o = 0 # while 문
    while n>0:
        n, o= n-1, 2*n-1+o

    return o

print(square(0))
print(square(1))
print(square(-2))
print(square(3))
print(square(-4))
print(square(5))
