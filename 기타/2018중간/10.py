def intersect(xs,ys):
    zs=[]
    for x in xs:
        if x in ys:
            zs.append(x)
    return zs

print(intersect([3,2,4],[1,2,3])) #[3,2]            
