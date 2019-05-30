def numbersArt(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end=' ')
        print()

numbersArt(5)

def numbersArt(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=' ')
        print()

numbersArt(5)

def numbersArt2(n):
    for i in range(n):
        for j in range(i):
                print(' ', end=' ')
        for k in range(i,n):
                print(k+1, end=' ')
        print()

numbersArt2(5)

def numbersArt3(n):
    for i in range(n,0,-1):
        for j in range(i,n+1):
            print(j, end=' ')
        print()

numbersArt3(5)

def numbersArt4(n):
    for i in range(n,0,-1):
        for j in range(1,i):
            print(' ', end=' ')
        for k in range(i,n+1):
            print(k, end=' ')
        print()

numbersArt4(5)
