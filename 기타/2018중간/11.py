def equiv_class(ns):
    ns.sort()
    if ns == []:
        return []
    else:
        top = ns[0]
        nss = [[top]]
        for n in ns[1:]:
            if n == top:
                nss[0] += [n]
            else:
                x = ns.index(n)
                if ns[x] > ns[x-1]:
                    nns += [[n]]
                elif: ns[x] == ns[x-1]:
                    nns[] +=
        return nss
