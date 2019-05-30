from cardgame import *

def blackjack():
    print("Welcome to SMaSH Casino!")
    username, tries, wins, chips, members = login(load_members())
    deck = fresh_deck()
    play_more = True
    while play_more == True:
        tries += 1
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
            wins += 1
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
                    print('chips=', chips)
                    play_more = more('Play more? (y/n)')
                    break

                hit_more = more('Hit more? (y/n)')

            if score_player <= 21:

                while score_dealer <= 16:
                        card, deck = hit(deck)
                        dealer.append(card)
                        score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")

                if score_dealer > 21:
                        chips += 1
                        wins += 1
                        print('I bust! You won.')

                else:
                        if score_dealer == score_player:
                            wins += 0.5
                            print('We draw')

                        elif score_dealer < score_player:
                            chips += 1
                            wins +=1
                            print('Yon won.')

                        else:
                            chips -= 1
                            print('I won.')

                print('chips=', chips)
                play_more = more('Play more? (y/n)')

    tries_today = tries - members[username][1]
    wins_today = wins - members[username][2]
    members[username] = (members[username][0],tries, wins, chips)
    store_members(members)
    print('You played', tries_today ,'games and won', wins_today ,'of them.')
    print('Your winning pecentage today is', "{0:.1f}".format(wins_today/tries_today*100) if tries_today> 0 else 0 ,'%')

    show_top5(members)

    print('Bye!')

blackjack()
