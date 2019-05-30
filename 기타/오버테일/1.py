def combination(n,k):
    if n == 0 or k == 0 :
        return 1
    elif n == k :
        return 1
    else:
        value = 1
        for x in range(0, k):
            value *= n-x
        for y in range(k,0,-1):
            value /= y
        return value

print(combination(5,3))
