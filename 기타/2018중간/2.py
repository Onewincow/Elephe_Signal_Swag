def search(key,ns):
    index = 0
    list = []
    for n in ns:
        if key == n:
            list += [index]
            index += 1
        else:
            index += 1
    if key not in ns:
        return []
    else:
        return list

print(search(3,[])) # []
print(search(3,[4,6,3,3,3])) # [2,3,4]
print(search(3,[3,3,3,3,3])) # [0,1,2,3,4]
print(search(3,[4,2,7,6,5])) # []
