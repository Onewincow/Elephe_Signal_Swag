def diff(xs,ys):
    zs=xs[:]
    for x in xs:
        if x in ys:
            zs.remove(x)
    return zs

print(diff([3,2,4],[1,2,3])) #[4]
