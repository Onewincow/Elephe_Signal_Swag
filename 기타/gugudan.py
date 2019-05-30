def gugudan1():
    for i in range(2,10):
       for j in range(2,6):
           print(i ,' x ', j,' = ', str(i*j).rjust(2), end='  ')
       print()
       for k in range(6,10):
           print(i ,' x ', k,' = ', str(i*k).rjust(2), end='  ')
       print()
    print()
print(gugudan1())

def gugudan1():
    for j in range(2,10):
       for i in range(2,6):
           print(i ,' x ', j,' = ', str(i*j).rjust(2), end='  ')
       print()
       for k in range(6,10):
           print(i ,' x ', k,' = ', str(i*k).rjust(2), end='  ')
       print()
    print()
print(gugudan2())
