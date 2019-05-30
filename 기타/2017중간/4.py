# -*- coding: utf-8 -*-

def remove(x,xs):
    if xs != '':
        if xs[0] == x:
            return remove(x,xs[1:])
        else:
            return xs[0] + remove(x,xs[1:])
    else:
        return ''

# 테스트 케이스
print(remove('a','abracadabra'))
print(remove('z','abracadabra'))

# 꼬리재귀함수
def removeT(x,xs):
    def loop(xs,ys):
        if xs != '':
            if xs[0] == x:
                return loop(xs[1:],ys)
            else:
                return loop(xs[1:],ys+xs[0])
        else:
            return ys
    return loop(xs,'')


# 테스트 케이스
print(removeT('a','abracadabra'))
print(removeT('z','abracadabra'))


# while 문 함수
def removeW(x,xs):
    ys = ''
    while xs != '':
        if xs[0] == x:
            xs = xs[1:]
        else:
            xs, ys = xs[1:], ys+xs[0]
    return ys

# 테스트 케이스
print(removeW('a','abracadabra'))
print(removeW('z','abracadabra'))
