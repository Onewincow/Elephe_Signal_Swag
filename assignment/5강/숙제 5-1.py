def searchWidestGap(list):
    t=0
    if list == [] :
        return (0,-1)

    elif len(list) == 1:
        return (0,0)

    for x in range(len(list)-2):
        a =abs(list[x]-list[x+1])
        b =abs(list[x+1]-list[x+2])
        if a>=b:
            if a>t:
                s=x
                t=a
        else:
            if b>t:
                s=x+1
                t=b

    return (t,s)


def searchWidestGap(ss):
    # assume that ss is sorted
    if len(ss) == 0:
        return -1, 0
    elif len(ss) == 1:
        return 0, 0
    else: # len(ss) >= 2
        widest = 0
        index = 0
        for i in range(len(ss)-1):
            gap = ss[i+1] - ss[i] # always >= 0
            if gap > widest:
                widest = gap
                index = i
        return index, widest

import random
def testSearchWidestGap():
    db = random.sample(range(500),100)
    print("Searching the widest gap...")
    db.sort()
    print(db)
    index, gap = searchWidestGap(db)
    print("The widest gap is:", gap)
    print("between", db[index], "and", db[index+1])
    print("at", index)
