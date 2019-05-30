class NegativeInteger (Exception): pass
class RBiggerThanN (Exception): pass

def combPascal():
    print('This program computes combination of two natural numbers, n and r.\n\
Press Control-C to quit.')
    enter = input('Press Enter when you are ready.')
    while enter != '':
        enter = input('Press Enter when you are ready.')
    while True:
        try:
            n = int(input('Enter n:'))
            if n < 0 : raise NegativeInteger
            r = int(input('Enter r:'))
            if r < 0 : raise NegativeInteger
            if n < r : raise RBiggerThanN
            matrix = [[]] * (n - r + 1)
            matrix[0] = [1] * (r + 1)
            for i in range(1, n - r + 1):
                matrix[i] = [1]
            for i in range(1, n - r + 1):
                for j in range(1, r + 1):
                    newvalue = matrix[i][j - 1] + matrix[i - 1][j]
                    matrix[i].append(newvalue)
            print(n,'C',r, ' = ', matrix[n-r][r],sep='')
        except ValueError:
            print ('enter the natural number.')
        except NegativeInteger:
            print ('not natural numbers.')
        except RBiggerThanN:
            print (r, 'is bigger than', n)
        except KeyboardInterrupt:
            print ('Goodbye!')
            break

combPascal()
