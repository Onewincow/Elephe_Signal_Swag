# -*- coding: utf-8 -*-

# 12. 이진수 시프트(좌우로 밀기) 연산

def shift(ds,move):
    ss = ds
    if move < 0:
        for _ in range(abs(move)):
            if len(ds) > abs(move):
                ss = ss[:-1]
            else:
                return '0'
    else:
        for _ in range(move):
            ss += '0'
    return ss

print(shift("11011",3)) # 11011000
print(shift("11011",2)) # 1101100
print(shift("11011",1)) # 110110
print(shift("11011",0)) # 11011
print(shift("11011",-1)) # 1101
print(shift("11011",-2)) # 110
print(shift("11011",-3)) # 11
print(shift("11011",-4)) # 1
print(shift("11011",-5)) # 0
print(shift("11011",-6)) # 0
