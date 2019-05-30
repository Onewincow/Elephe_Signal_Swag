# -*- coding: utf-8 -*-

### 4. 일반재귀 함수를 꼬리재귀 함수로 변환하기

def updown(ns):
    if ns != []:
        if ns[0] % 2 == 0:
            return [ns[0]//2] + updown(ns[1:])
        else:
            return [ns[0]*2] + updown(ns[1:])
    else:
        return []

print(updown([4, 6,  5, 3,  7, 6, 2, 1, 3, 2])) #[2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
print(updown([14, 69, 87, 13, 0, 16, 83, 19, 45, 88])) #[7, 138, 174, 26, 0, 8, 166, 38, 90, 44]

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

print(updownT([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
# #            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
print(updownT([14, 69, 87, 13, 0, 16, 83, 19, 45, 88]))
# #            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]
