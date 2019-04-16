def smallest(x,y,z):
    return smaller

def smallest(x,y,z):
    if x>y:
        if y>z:
            return z
        else :
            return y
    elif y>z:
        if z>x:
            return x
        else:
            return z
    elif z>x:
        if x>y:
            return y
        else:
            return x
    else :
        return x

print(smallest(3,5,9)) # returns 3
print(smallest(5,3,9)) # returns 3
print(smallest(5,9,3)) # returns 3
print(smallest(3,9,5)) # returns 3
print(smallest(9,3,5)) # returns 3
print(smallest(9,5,3)) # returns 3
print(smallest(3,3,5)) # returns 3
print(smallest(5,3,3)) # returns 3
print(smallest(3,5,3)) # returns 3
print(smallest(3,3,3)) # returns 3  
