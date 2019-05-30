def union(xs,ys):
    zs=[]
    for x in xs:
        if x not in zs:
             zs.append(x)
    for y in ys:
        if y not in zs:
            zs.append(y)
    return zs

print(union([3,2,4],[1,2,3])) #[4,1,2,3]
