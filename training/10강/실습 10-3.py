class RangeOneError (Exception): pass

def input_float():
    while True:
        try:
            x = float(input('enter the float of which range is -1.0 ~ 1.0.'))
            if not (-1 <= x <= 1): raise RangeOneError
        except ValueError as e:
            print(e, "is not float.")
        except RangeOneError:
            print (x, "is out of range.")
        else:
            print(x, "is float.")
            break

input_float()
