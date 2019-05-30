def binSearchClosest(list,key):
    if list == [] :
        return None
    elif len(list) == 1 :
        return 0
    t=key**10
    for x in range(len(list)-1) :
        a= abs(key - list[x])
        b= abs(key - list[x+1])
        if a <= b :
            if t > a :
                s = x
                t = a
        else :
            if t > b:
                s = x+1
                t = b
    return s


def binSearchClosest(list,number):
    a=[]
    b=[]
    if list==[]:
        return None
    for n in range(len(list)):
        gap=abs(number-list[n])
        a.append(gap)
        x=min(a)
        b.append(x)
    y=b.index(x)
    return y



def binSearchClosest(ss,key):
    low = 0
    high = highest = len(ss) - 1
    while low <= high:
        mid = (high + low) // 2
        if key == ss[mid]:
            return mid
        elif key < ss[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if high < 0:
        high = 0
    if low > highest:
        low = highest
    diffLow = abs(key - ss[low])
    diffHigh = abs(key - ss[high])
    if diffLow == diffHigh:
        if ss[low] <= ss[high]:
            return low
        else:
            return high
    elif diffLow < diffHigh:
        return low
    else:
        return high

import random
def testBinSearchClosest():
    db = random.sample(range(500),100)
    print("Binary search closest function test")
    db.sort()
    print(db)
    for _ in range(10):
        key = random.randrange(500)
        index = binSearchClosest(db, key)
        print("The closest value to", key, ":", db[index], "at index", index)
    key = random.randrange(10000)    
