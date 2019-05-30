from cardgame import *

def blackjack():
    print("Welcome to SMaSH Casino!")
    deck = fresh_deck()
    chips = 0
    play_more = True
    while play_more == True:
        print('-----')
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        print("My cards are:")
        print(" ", "****", "**")
        print(" ", dealer[1]["suit"], dealer[1]["rank"])
        show_cards(player, "Your cards are:")
        score_player = count_score(player)
        score_dealer = count_score(dealer)

        if score_player == 21:
            chips += 2
            print('Blackjack! You won.')
            print('chips=', chips)
            play_more = more('Play more? (y/n)')

        else:
            hit_more = more('Hit more? (y/n)')
            while hit_more == True :
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(' ', card['suit'], card['rank'])

                if score_player > 21:
                    chips -= 1
                    print('You bust! I won.')
                    break

                hit_more = more('Hit more? (y/n)')

            while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
            show_cards(dealer, "My cards are:")

            if score_dealer > 21:
                    chips += 1
                    print('I bust! You won.')

            else:
                    if score_dealer == score_player:
                        print('We draw')

                    elif score_dealer < score_player:
                        chips += 1
                        print('Yon won.')

                    else:
                        chips -= 1
                        print('I won.')

        print('chips=', chips)
        play_more = more('Play more? (y/n)')

    print('Bye!')

blackjack()
