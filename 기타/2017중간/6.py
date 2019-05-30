def drop_before(s,index):
    if s != [] and index > 0:
        return drop_before(s[1:],index-1)
    else:
        return s

def drop_before(s,index):
    while s!=[] and index>0:
        s, index = s[1:], index-1
    return s

s = [1,2,3,4,5]
print("s")
print("drop_before(s,0) =", drop_before(s,0)) # => [1,2,3,4,5]
print("drop_before(s,1) =", drop_before(s,1)) # => [2,3,4,5]
print("drop_before(s,2) =", drop_before(s,2)) # => [3,4,5]
print("drop_before(s,3) =", drop_before(s,3)) # => [4,5]
print("drop_before(s,4) =", drop_before(s,4)) # => [5]
print("drop_before(s,5) =", drop_before(s,5)) # => []
print("drop_before(s,6) =", drop_before(s,6)) # => []
print("drop_before(s,-3) =", drop_before(s,-3)) # => [1,2,3,4,5]
print("drop_before([],4) =", drop_before([],4)) # => []



def take_before(s,index):
    if s!= [] and index<0:
        return take_before(s[:-1], index-1)
    else:
        return s
def take_before(s,index):
    pass  # 꼬리 재귀

def take_before(s,index):
    pass  # while 문


# s = [1,2,3,4,5]
# print("take_before(s,0) =", take_before(s,0)) # => []
# print("take_before(s,1) =", take_before(s,1)) # => [1]
# print("take_before(s,2) =", take_before(s,2)) # => [1,2]
# print("take_before(s,3) =", take_before(s,3)) # => [1,2,3]
# print("take_before(s,4) =", take_before(s,4)) # => [1,2,3,4]
# print("take_before(s,5) =", take_before(s,5)) # => [1,2,3,4,5]
# print("take_before(s,6) =", take_before(s,6)) # => [1,2,3,4,5]
# print("take_before([],4) =", take_before([],4)) # => []
# print("take_before(s,-3) =", take_before(s,-3)) # => []
