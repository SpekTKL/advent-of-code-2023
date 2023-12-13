

def get_input(file):
    with open(file, mode='r', encoding='utf-8') as f:
        return f.readlines()


def part_2(scratch_cards):
    copies_won = {
        '1': 1
    }

    cards = []

    for card in scratch_cards:
        card_elems = card.split(':')
        card_id = card_elems[0].replace('   ', ' ').replace('  ', ' ').split(' ')[1]

        cards.append(int(card_id))

        card_numbers = get_card_numbers(card)
        winning_numbers = card_numbers[0]
        numbers_on_card = card_numbers[1]

        winning_count = get_winning_count(numbers_on_card, winning_numbers)

        if winning_count != 0:
            copies_won[card_id] = winning_count
        else:
            copies_won[card_id] = 0

    for card in cards:
        next_card = card + 1
        final_card = card + copies_won.get(str(card))
        for i in range(next_card, final_card + 1):
            cards.append(i)

    print(f"The total number of cards is: {len(cards)}")


def get_card_numbers(card):
    card_numbers = card.split(':')[1].strip().split('|')
    winning_numbers = card_numbers[0].replace('  ', ' ').split(' ')
    numbers_on_card = card_numbers[1].strip().replace('  ', ' ').split(' ')
    return winning_numbers, numbers_on_card


def get_winning_count(numbers, winning_numbers):
    count = 0

    for number in numbers:
        if number in winning_numbers:
            count += 1

    return count


def part_1(scratch_cards):
    total_points = 0
    for card in scratch_cards:
        card_numbers = get_card_numbers(card)
        winning_numbers = card_numbers[0]
        numbers_on_card = card_numbers[1]

        winning_count = get_winning_count(numbers_on_card, winning_numbers)

        if winning_count != 0:
            total_points += 2 ** (winning_count - 1)

    print(f"The total number of points is: {total_points}")


def main():
    scratch_cards = get_input('input-04.txt')
    part_1(scratch_cards)
    part_2(scratch_cards)


main()
