#def isinteger(s):
#    return s.isdigit() or s[0] == '-' and s[1:].isdigit()
def isfloat(s):
    t = s.partition('.')
    if '.' > t[0] >= '-' :
        return (t[2].isdigit() or t[2] == '')

    elif t[0].isdigit()  :
        return (t[2].isdigit() or t[2] == '')

    elif t[0] == '' :
        return t[2].isdigit()

    else :
        return False

print(isfloat(".112"))	#True
print(isfloat("-.112"))	#True
print(isfloat("3.14"))	#True
print(isfloat("-3.14"))	#True
print(isfloat("5."))	#True
print(isfloat("5.0"))	#True
print(isfloat("-777.0"))	#True
print(isfloat("-777."))	#True
print(isfloat("."))	#False
print(isfloat(".."))	#False
