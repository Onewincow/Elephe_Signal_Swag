def permutation0(n,k):
    if k > 0:
        return n * permutation0(n-1,k-1)
    else:
        return 1

def permutation1(n,k):
    def loop(n, k,f):
        if k > 0:
            return loop(n-1,k-1,f*n)
        else:
            return f
    return loop(n, k,1)

def permutation2(n,k):
    f = 1
    while k > 0:
        n, k, f = n-1, k-1, f*n
    return f

def permutation3(n,k) :
    f = 1
    for _ in range(k):
        f *= n
        n=n-1
    return f

print(permutation3(1,1)) # => 1
print(permutation3(2,1)) # => 2
print(permutation3(2,2)) # => 2
print(permutation3(3,1)) # => 3
print(permutation3(3,2)) # => 6
print(permutation3(3,3)) # => 6
print(permutation3(4,1)) # => 4
print(permutation3(4,2)) # => 12
print(permutation3(4,3)) # => 24
print(permutation3(4,4)) # => 24
