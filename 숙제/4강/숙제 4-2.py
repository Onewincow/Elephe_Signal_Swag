def radixsort(ds,length):
    master=[[],[],[],[],[],[],[],[],[],[]]
    for x in range(length-1,-1,-1):
        for y in ds:
            for z in y[x]:
                master[int(z)]+=[y]
        ds[:]=[]
        for w in range(10):
            ds += master[w]
        master=[[],[],[],[],[],[],[],[],[],[]]
    return ds

print(radixsort(["170",'045','075','090','002','024','802','066'],3))
