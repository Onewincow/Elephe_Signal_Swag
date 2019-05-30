def insertionsort(ns) :
    ss = []
    while ns != []:
        ns, ss = ns[1:],insert(ns[0],ss)
    return ss

def insert(n,ss):
    def loop(ss,left):
        if ss != []:
            if n <= ss[0]:
                return left+[n]+ss
            else:
                return loop(ss[1:],left+[ss[0]])
        else:
            return left+[n]
    return loop(ss,[])
