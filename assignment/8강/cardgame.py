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
