# -*- coding: utf-8 -*-

### 3. 비감소 리스트 확인

def nondecreasing(ns):
    if len(ns) > 1:
        if ns[0] > ns[1]:
            return False
        else:
            return nondecreasing(ns[1:])
    else:
        return True

print(nondecreasing([])) # True
print(nondecreasing([3])) # True
print(nondecreasing([3,3])) # True
print(nondecreasing([3,4,5,5,8,9])) # True
print(nondecreasing([3,4,3,3,8,9])) # False
print(nondecreasing([1,3,5,14,22,59,59])) # True
print(nondecreasing([1,3,5,14,22,59,58])) # False
