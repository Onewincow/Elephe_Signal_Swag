# -*- coding: utf-8 -*-
def is_pal(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_pal(s[1:-1])

def is_pal(s):
    return len(s) <= 1 or (s[0] == s[-1] and is_pal(s[1:-1]))

# 테스트 케이스
print(is_pal("")) # True
print(is_pal("a")) # True
print(is_pal("aa")) # True
print(is_pal("aba")) # True
print(is_pal("abba")) # True
print(is_pal("aaba")) # False
print(is_pal("abcba")) # True
print(is_pal("여보 안경 안 보여")) # False
print(is_pal("여보안경안보여")) # True
