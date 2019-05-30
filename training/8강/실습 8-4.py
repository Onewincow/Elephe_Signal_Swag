# -*- coding: utf-8 -*-
def show_cards(cards,message):
    print(message)
    for card in cards:
        print ( card['suit'], card['rank'])


cards = [{'rank': 3, 'suit': 'Club'}]
show_cards(cards, '')

cards = [{'rank': 3, 'suit': 'Club'}, {'rank': 7, 'suit': 'Spade'}, {'rank': 9, 'suit': 'Club'}, {'rank': 3, 'suit': 'Daiamond'}]
show_cards(cards,'내 카드는')
