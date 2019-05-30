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
