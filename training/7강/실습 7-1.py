# -*- coding: utf-8 -*-
import random
def create_board():
    seed = [1,2,3,4]
    random.shuffle(seed)
    sprout = [seed[2], seed[3], seed[0], seed[1]]
    stem = [seed[1], seed[0], seed[3], seed[2] ]
    flower = [seed[3], seed[2], seed[1], seed[0] ]
    return [seed, sprout, stem, flower]

print(create_board())
