from collections import Counter

MAPPING_ORDER = {
    'T': 'A',
    'J': '.',
    'Q': 'C',
    'K': 'D',
    'A': 'E'
    }


def find_all_combinations(hand):
    if not hand:
        return [""]

    current_card = hand[0]
    if current_card == 'J':
        possible_values = "23456789TQKA"
    else:
        possible_values = current_card

    combinations = [
        first_half + second_half
        for first_half in possible_values
        for second_half in find_all_combinations(hand[1:])
    ]

    return combinations


def find_max_type(hand):
    return max(map(get_type, find_all_combinations(hand)))


def get_type(hand):
    counts = Counter(hand)

    #  6 - Five of a kind
    #  5 - Four of a kind
    #  4 - Full House
    #  3 - Three of a kind
    #  2 - Two Pair
    #  1 - One Pair
    #  0 - Highest Card

    if len(counts) == 1:
        return 6
    if len(counts) == 2:
        if 4 in counts.values():
            return 5
        if 3 in counts.values() and 2 in counts.values():
            return 4
    if len(counts) == 3:
        if 3 in counts.values() and list(counts.values()).count(1) == 2:
            return 3
        if list(counts.values()).count(2) == 2:
            return 2
    if len(counts) == 4:
        return 1

    return 0


def get_order(hand):
    return [MAPPING_ORDER.get(card, card) for card in hand]


def sort_func(hand):
    return find_max_type(hand), get_order(hand)


def main(file):
    plays = []
    with open(file, 'r') as file:
        hands = file.read().split('\n')
        for hand in hands:
            cards, bid = hand.split()
            plays.append((cards, int(bid)))

    plays.sort(key=lambda play: sort_func(play[0]))

    total_winnings = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        total_winnings += bid * rank

    print(f'The total winnings are: {total_winnings}')


if __name__ == '__main__':
    main('07-ex.txt')
    main('07-input.txt')
