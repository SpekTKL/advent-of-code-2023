CHARACTERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
valid_numbers = []

DIRECTIONS = [
    (-1, -1),  # Top Left
    (-1, 0),   # Up
    (-1, 1),   # Top Right
    (0, -1),   # Left
    (0, 1),    # Right
    (1, -1),   # Bottom Left
    (1, 0),    # Down
    (1, 1),    # Bottom Right
]


def get_sum_of_gear_ratios(matrix):
    total_sum = 0
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            total_sum += _get_gear_ratio(matrix, i, j) if col == '*' else 0

    return total_sum


def _get_gear_ratio(matrix, row, col):
    adjacent_numbers = []
    for dx, dy in DIRECTIONS:
        adjacent_row, adjacent_col = row + dx, col + dy
        if 0 <= adjacent_row < len(matrix) and 0 <= adjacent_col < len(matrix[adjacent_row]):
            if matrix[adjacent_row][adjacent_col].isdigit():
                part_number = _get_full_part_number(matrix, adjacent_row, adjacent_col)
                if part_number not in adjacent_numbers:
                    adjacent_numbers.append(part_number)

    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]

    return 0


def _get_full_part_number(matrix, row, col):
    number_str = matrix[row][col]

    left_col = col - 1
    while left_col >= 0 and matrix[row][left_col].isdigit():
        number_str = matrix[row][left_col] + number_str
        left_col -= 1

    right_col = col + 1
    while right_col < len(matrix[row]) and matrix[row][right_col].isdigit():
        number_str += matrix[row][right_col]
        right_col += 1

    return int(number_str)


def get_above(matrix, row, min_col, max_col):
    above = []
    if row == 0:
        return above
    if min_col == 0:
        min_col += 1
    if max_col == len(matrix[row]) - 1:
        max_col -= 1

    for i in range(min_col - 1, max_col + 2):
        above.append(matrix[row - 1][i])

    return above


def get_inline(matrix, row, min_col, max_col):
    inline = []
    if min_col == 0 and max_col == len(matrix[row]) - 1:
        return inline
    elif min_col == 0:
        inline.append(matrix[row][max_col + 1])
        return inline
    elif max_col == len(matrix[row]) - 1:
        inline.append(matrix[row][min_col - 1])
        return inline
    else:
        inline.append(matrix[row][min_col - 1])
        inline.append(matrix[row][max_col + 1])
        return inline


def get_below(matrix, row, min_col, max_col):
    below = []
    if row == len(matrix) - 1:
        return below
    if min_col == 0:
        min_col += 1
    if max_col == len(matrix[row]) - 1:
        max_col -= 1

    for i in range(min_col - 1, max_col + 2):
        below.append(matrix[row + 1][i])

    return below


def get_surrounding(matrix, row, min_col, max_col):
    surrounding = []
    surrounding += get_above(matrix, row, min_col, max_col)
    surrounding += get_inline(matrix, row, min_col, max_col)
    surrounding += get_below(matrix, row, min_col, max_col)

    return surrounding


def check_surrounding(surrounding):
    for c in surrounding:
        if c not in CHARACTERS:
            return True

    return False


def main():
    with open('input-day03', 'r', encoding='utf-8') as file:
        matrix = file.readlines()
        for i, row in enumerate(matrix):
            number = ''

            matrix[i] = row[:-1]
            min_col = -1

            for j, col in enumerate(row):
                if col.isdigit() and (j == 0 or min_col == -1):
                    min_col = j
                    number += col
                    continue
                if col.isdigit() and min_col != -1:
                    number += col
                    continue
                if not col.isdigit():
                    max_col = j - 1
                    if min_col != -1:
                        surrounding = get_surrounding(matrix, i, min_col, max_col)
                        is_valid = check_surrounding(surrounding)
                        if is_valid:
                            valid_numbers.append(int(number))

                    number = ''
                    min_col = -1
                    continue

    if number != '':
        row = len(matrix) - 1
        min_col = len(matrix[row]) - len(number) - 1
        max_col = len(matrix[row]) - 1
        surrounding = get_surrounding(matrix, row, min_col, max_col)
        is_valid = check_surrounding(surrounding)
        if is_valid:
            valid_numbers.append(int(number))


if __name__ == '__main__':
    # main()
    with open('input-day03', 'r') as file:
        matrix = file.readlines()

    print(get_sum_of_gear_ratios(matrix))
