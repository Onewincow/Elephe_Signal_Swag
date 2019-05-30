# -*- coding: utf-8 -*-
import random
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for a in suits:
        for s in ranks:
            deck += [{"suit":a,"rank":s}]
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0],deck[1:])

def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        if card['rank'] != 'A':
            if card['rank'] == 'J'or card['rank'] =='Q'or card['rank'] =='K':
                score += 10
            else:
                score += card['rank']

        else:
            number_of_ace += 1
            score += 11

    while score >21 and number_of_ace>0:
        score -= 10
        number_of_ace -= 1

    return score

def show_cards(cards,message):
    print(message)
    for card in cards:
        print (' ', card['suit'], card['rank'])

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + '\n'
        file.write(line)
    file.close()

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

def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(), key= lambda x:x[1][3], reverse = True)
    print("All-time Top 5 based on the number of chips earned")
    if len(sorted_members) < 5:
    	for i in range(len(sorted_members)):
    			if(sorted_list[i][1][3] > 0):
    				print(str(i+1) + '.', sorted_members[i][0] ,":", sorted_members[i][1][3])
    else :
    	for i in range(5):
    		if(sorted_members[i][1][3] > 0):
    			print(str(i+1) + '.', sorted_members[i][0] ,":", sorted_members[i][1][3])
