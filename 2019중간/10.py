# -*- coding: utf-8 -*-

# 10 아이소그램 확인

def isisogram(word):
    if len(word) >1:
        for x in range(len(word)-1):
            for y in range(x, len(word)):
                if x!=y:
                    if word[x] == word[y]:
                        return False
    return True

print(isisogram("")) # True
print(isisogram("a")) # True
print(isisogram("aa")) # False
print(isisogram("and")) # True
print(isisogram("hanyang")) # False
print(isisogram("playground")) # True
print(isisogram("uncopyrightables")) # True
