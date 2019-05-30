# -*- coding: utf-8 -*-

def updownW(ns):
    ss = []
    while ns != []:
        if ns[0] % 2 == 0:
            ss.append(ns[0]//2)
        else:
            ss.append(ns[0]*2)
        ns = ns[1:]
    return ss

### 6. for 루프 함수로 만들기

def updownF(ns):
    ss = []
    for x in range(len(ns)):
        if ns[x] % 2 == 0:
            ss.append(ns[x]//2)
        else:
            ss.append(ns[x]*2)
    return ss

print(updownF([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
# #            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
print(updownF([14, 69, 87, 13, 0, 16, 83, 19, 45, 88]))
# #            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]
