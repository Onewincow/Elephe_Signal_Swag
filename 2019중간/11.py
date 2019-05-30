# -*- coding: utf-8 -*-

### 11. 짝 찾기
def findAllPairs(ns,n):
    pairs = []
    if len(ns) >1:
        for x in range(len(ns)-1):
            for y in range(x, len(ns)):
                if x!=y:
                    if ns[x] + ns[y] == n:
                        pairs += [(x,y)]
    return pairs

print(findAllPairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],10))
# # [(0, 1), (0, 5), (3, 4), (4, 8)]
print(findAllPairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],5))
# # [(0, 7), (3, 6), (3, 9), (6, 8), (8, 9)]
print(findAllPairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],7))
# # [(0, 3), (0, 8), (1, 7), (2, 6), (2, 9), (5, 7)]
