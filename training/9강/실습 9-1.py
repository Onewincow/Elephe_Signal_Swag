members = {"doh": ("sid73", 994, 550, 35), "didi": ("edd484", 130, 55, 10), "hy": ("er878re", 35, 18, 2), "dr": ("qwert", 18, 0, -5),"who": ("poiuy", 34, 18, 0)}

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members.keys():
        if trypasswd == members[username][0]:
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]

            print('You played', tries, 'games and won', wins,'of them.')
            print('Your all-time winning percentage is', "{0:.1f}".format(wins/tries*100) if tries> 0 else 0 ,'%')
            if chips >=0:
                print('You have', chips,'chips.')
            else:
                print('You owe', abs(chips),'chips.')
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd, 0, 0, 0)
        return username, 0, 0, 0, members
