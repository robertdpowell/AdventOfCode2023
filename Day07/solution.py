input = open('input.txt').read()
strengths = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}
joker_strengths = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}
def check_cards(cards):
    cards_list = []
    card_counts = {}
    for card in cards:
        card_count = cards.count(card)
        cards_list.append(card)
        card_counts[card] = card_count

    if all(card == cards_list[0] for card in cards_list):
        return 'five of a kind'

    elif len(set(cards)) == len(cards):
        return 'high card'

    else:
        for card, card_count in card_counts.items():
            if card_count == 4:
                return 'four of a kind'
            elif card_count == 3 and len(set(cards_list)) == 3:
                return 'three of a kind'
            elif card_count == 2 and len(set(cards_list)) == 4:
                return 'one pair'
            elif card_count == 2 and len(set(cards_list)) == 3:
                return 'two pair'
            elif card_count == 3 and len(set(cards_list)) == 2:
                return 'full house'

def check_joker_cards(cards):
    cards_list = []
    card_counts = {}
    joker_count = 0
    for card in cards:
        card_count = cards.count(card)
        cards_list.append(card)
        card_counts[card] = card_count
        if card == 'J':
            joker_count += 1

    has_pair = any(count == 2 for count in card_counts.values())
    has_three_of_a_kind = any(count == 3 for count in card_counts.values())

    if joker_count == 0:
        if all(card == cards_list[0] for card in cards_list):
            return 'five of a kind'
        elif len(set(cards)) == len(cards):
            return 'high card'
        else:
            for card, card_count in card_counts.items():
                if card_count == 4:
                    return 'four of a kind'
                elif card_count == 3 and len(set(cards_list)) == 3:
                    return 'three of a kind'
                elif card_count == 2 and len(set(cards_list)) == 4:
                    return 'one pair'
                elif card_count == 2 and len(set(cards_list)) == 3:
                    return 'two pair'
                elif card_count == 3 and len(set(cards_list)) == 2:
                    return 'full house'

    elif joker_count == 1:
        print(cards)
        if len(set(cards_list)) == 2:
            print(f'five of a kind because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'five of a kind'

        elif len(set(cards_list)) == 3 and has_pair:
            print(f'full house because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'full house'
        elif len(set(cards_list)) == 3 and has_three_of_a_kind:
            print(f'four of a kind because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'four of a kind'
        elif len(set(cards_list)) == 4:
            print(f'three of a kind because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'three of a kind'
        elif len(set(cards_list)) == 5:
            print(f'one pair because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'one pair'


    elif joker_count == 2:
        print(cards)
        if len(set(cards_list)) == 2:
            print(f'five of a kind because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'five of a kind'
        elif len(set(cards_list)) == 3:
            print(f'four of a kind because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'four of a kind'
        elif len(set(cards_list)) == 4:
            print(f'three of a kind because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'three of a kind'

    elif joker_count == 3:
        print(cards)
        if len(set(cards_list)) == 2:
            print(f'five of a kind because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'five of a kind'
        elif len(set(cards_list)) == 3:
            print(f'four of a kind because set length is {len(set(cards_list))} and joker count is {joker_count}')
            return 'four of a kind'

    elif joker_count == 4:
        print(cards)
        print(f'five of a kind because joker count is {joker_count}')
        return 'five of a kind'

    elif joker_count == 5:
        print(cards)
        print(f'five of a kind because joker count is {joker_count}')
        return 'five of a kind'

def replace_card_with_strength(card):
    if card in strengths:
        return strengths[card]
    else:
        return int(card)

def replace_card_with_joker_strength(card):
    if card in joker_strengths:
        return joker_strengths[card]
    else:
        return int(card)
def solve1():
    hands_with_strength = []
    hands = input.split('\n')
    for hand in hands:
        replaced_cards = []
        hand = hand.split()
        cards = hand[0]
        score = hand[1]
        result = check_cards(cards)
        strength = 0
        if result == 'five of a kind':
            strength = 7

        elif result == 'four of a kind':
            strength = 6

        elif result == 'full house':
            strength = 5

        elif result == 'three of a kind':
            strength = 4

        elif result == 'two pair':
            strength = 3

        elif result == 'one pair':
            strength = 2

        elif result == 'high card':
            strength = 1

        replaced_cards.append(strength)
        for card in cards:
            card = replace_card_with_strength(card)
            replaced_cards.append(card)

        hands_with_strength.append((cards, replaced_cards, score))

    sorted_hands = sorted(hands_with_strength, key=lambda x: x[1])
    scores = []

    for sorted_hand in sorted_hands:
        rank = int(sorted_hands.index(sorted_hand) + 1)
        score = int(sorted_hand[2])
        final_score = rank * score
        scores.append(final_score)
    return (sum(scores))


def solve2():
    hands_with_strength = []
    hands = input.split('\n')
    for hand in hands:
        replaced_cards = []
        hand = hand.split()
        cards = hand[0]
        score = hand[1]
        result = check_joker_cards(cards)
        strength = 0
        if result == 'five of a kind':
            strength = 7

        elif result == 'four of a kind':
            strength = 6

        elif result == 'full house':
            strength = 5

        elif result == 'three of a kind':
            strength = 4

        elif result == 'two pair':
            strength = 3

        elif result == 'one pair':
            strength = 2

        elif result == 'high card':
            strength = 1

        replaced_cards.append(strength)
        for card in cards:
            card = replace_card_with_joker_strength(card)
            replaced_cards.append(card)

        hands_with_strength.append((cards, replaced_cards, score))

    sorted_hands = sorted(hands_with_strength, key=lambda x: x[1])
    print (len(sorted_hands))
    for sorted_hand in sorted_hands:
        print (sorted_hand)
    scores = []

    for sorted_hand in sorted_hands:
        rank = int(sorted_hands.index(sorted_hand) + 1)
        score = int(sorted_hand[2])
        final_score = rank * score
        print (f'rank is {rank}, score is {score}, final score is {final_score}')
        scores.append(final_score)
    return (sum(scores))

print (f'solution 1 answer is {solve1()}')
print (f'solution 2 answer is {solve2()}')
