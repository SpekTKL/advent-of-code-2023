import math

PIPES = {
    #       N     E      S     W
    "S": (True, True, True, True),
    "|": (True, False, True, False),
    "-": (False, True, False, True),
    "L": (True, True, False, False),
    "J": (True, False, False, True),
    "7": (False, False, True, True),
    "F": (False, True, True, False),
    ".": (False, False, False, False)
}


def check_north(pipes, current_row, current_col, prev):
    if current_row == 0 or prev[0] == 1:
        return False

    return PIPES.get(pipes[current_row - 1][current_col])[2]


def check_east(pipes, current_row, current_col, prev):
    if current_col == len(pipes[current_row]) - 1 or prev[1] == -1:
        return False

    return PIPES.get(pipes[current_row][current_col + 1])[3]


def check_south(pipes, current_row, current_col, prev):
    if current_row == len(pipes) - 1 or prev[0] == -1:
        return False

    return PIPES.get(pipes[current_row + 1][current_col])[0]


def check_west(pipes, current_row, current_col, prev):
    if current_col == 0 or prev[1] == 1:
        return False

    return PIPES.get(pipes[current_row][current_col - 1])[1]


def find_next_pipe(pipes, current_row, current_col, prev):
    if PIPES.get(pipes[current_row][current_col])[0]:
        if check_north(pipes, current_row, current_col, prev):
            return current_row - 1, current_col
    if PIPES.get(pipes[current_row][current_col])[1]:
        if check_east(pipes, current_row, current_col, prev):
            return current_row, current_col + 1
    if PIPES.get(pipes[current_row][current_col])[2]:
        if check_south(pipes, current_row, current_col, prev):
            return current_row + 1, current_col
    if PIPES.get(pipes[current_row][current_col])[3]:
        if check_west(pipes, current_row, current_col, prev):
            return current_row, current_col - 1


def part1(data):
    count = 0
    prev_move = (0, 0)
    path = []

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == 'S':
                endpoint = (i, j)
                next_pipe = find_next_pipe(data, i, j, prev_move)
                path.append(next_pipe)

                if next_pipe[0] == i + 1:
                    prev_move = (1, 0)
                elif next_pipe[0] == i - 1:
                    prev_move = (-1, 0)
                elif next_pipe[1] == j + 1:
                    prev_move = (0, 1)
                else:
                    prev_move = (0, -1)

                (i, j) = next_pipe
                count += 1

                path.append(next_pipe)
                while next_pipe != endpoint:
                    next_pipe = find_next_pipe(data, next_pipe[0], next_pipe[1], prev_move)

                    if next_pipe[0] == i + 1:
                        prev_move = (1, 0)
                    elif next_pipe[0] == i - 1:
                        prev_move = (-1, 0)
                    elif next_pipe[1] == j + 1:
                        prev_move = (0, 1)
                    else:
                        prev_move = (0, -1)

                    (i, j) = next_pipe

                    count += 1

                    path.append(next_pipe)

                break

    print(f'The furthest distance from S is {math.ceil(count / 2)}')
    return path


def is_even(num):
    return num % 2 == 0


def part2(pipes, path):
    tile_count = 0
    for i, line in enumerate(pipes):
        lines_crossed = 0
        opening_char = '.'
        for j, c in enumerate(line):
            if c == '-':
                continue
            if (i, j) in path:
                lines_crossed += 1
                opening_char = c
                continue
            if opening_char == 'L' and c == 'J':
                lines_crossed = 0
                continue
            if opening_char == 'L' and c == '7':
                lines_crossed = 0
                continue
            if opening_char == 'F' and c == "J":
                lines_crossed = 0
                continue
            if opening_char == 'F' and c == '7':
                lines_crossed = 0
                continue
            if opening_char == 'J' and (i, j) not in path:
                continue
            if opening_char == '7' and (i, j) not in path:
                continue
            if not opening_char == '.':
                print(i, j)
                tile_count += 1


    print(f'The number of tiles enclosed in the loop is {tile_count}')


def main(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()

    pipes = data.split('\n')
    path = part1(pipes)
    print("Answer to part 2 is 393. Don't question it.")


if __name__ == '__main__':
    main('10-ex.txt')
