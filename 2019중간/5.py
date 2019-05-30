# -*- coding: utf-8 -*-

### 5. 꼬리재귀 함수를 while 루프 함수로 변환하기
def updownT(ns):
    def loop(ns,ss):
        if ns != []:
            if ns[0] % 2 == 0:
                ss.append(ns[0]//2)
                return loop(ns[1:],ss)
            else:
                ss.append(ns[0]*2)
                return loop(ns[1:],ss)
        else:
            return ss
    return loop(ns,[])


def updownW(ns):
    ss = []
    while ns != []:
        if ns[0] % 2 == 0:
            ss.append(ns[0]//2)
        else:
            ss.append(ns[0]*2)
        ns = ns[1:]
    return ss

print(updownW([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
# #            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
print(updownW([14, 69, 87, 13, 0, 16, 83, 19, 45, 88]))
# #            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]
