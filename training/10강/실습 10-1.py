def input_float():
    while True:
        try:
            x = float(input('enter the float.'))
        except ValueError as e:
            print(e, "is not float.")
        else:
            print(x, "is float.")
            break
        finally:
            print("bye.")

input_float()
