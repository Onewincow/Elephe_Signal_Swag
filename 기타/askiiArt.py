def asciiArt(n):
    for i in range(n):
        for j in range(n):
            print('#', end=' ')
        print()

asciiArt(5)

def asciiArtCross(n):
    for i in range(n):
        for j in range(n):
            if i == n//2:
                print('#', end=' ')
            else:
                if j == n//2:
                    print('#', end=' ')
                else:
                    print(' ', end=' ')
        print()

asciiArtCross(5)


def asciiArtX(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print('#', end=' ')
            elif j +i == n-1:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()

asciiArtX(5)


def asciiArtSqure(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1:
                print('#', end=' ')
            else:
                if j == 0 or j == n-1:
                    print('#', end=' ')
                else:
                    print(' ', end=' ')
        print()

asciiArtSqure(5)


def asciiArtDiamond(n):
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n-1) and j==n//2:
                print('#', end=' ')
            else:
                if j=n//2-i or j==n//2+i or j == n//2 - i:
                    print('#', end=' ')
                else:
                    print(' ', end=' ')
        print()

asciiArtSqure(5)
