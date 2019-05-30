number_of_door = int(input('))
first = int(input())
if number_of_door >= 6:
    print('Love is open door')
else:
    for _ in range(number_of_door-1):
        if first == 1:
            print(0)
            first -= 1
        else:
            print(1)
            first +=1
