def insertionsort(ns):
    def loop(ns,ss):
        if ns != []:
            return loop(ns[1:],insert(ns[0],ss))
        else:
            return ss
    return loop(ns,[])


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
