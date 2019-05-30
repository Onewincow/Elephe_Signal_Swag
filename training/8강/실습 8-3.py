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
            if score < 11:
                score += 11
            else:
                score += 1

    if score > 21 :
        score -= 10

    return score
