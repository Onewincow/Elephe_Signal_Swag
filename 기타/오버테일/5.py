def rle(str):
    n = 1
    list = []
    for x in range(len(str)-1):
        if str[x] == str [x+1]:
            n = n+1
        else:
            list += [ n+1  str[x]]
            n = 1
    return list

print(rle('wwwbbb'))
