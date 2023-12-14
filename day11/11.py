from itertools import combinations
from collections import defaultdict


def check_cols(galaxy):
    empty_cols = []
    row_length = len(galaxy[0])

    for i in range(row_length):
        galaxy_count = 0
        for row in galaxy:
            if row[i] == '#':
                galaxy_count += 1

        if galaxy_count == 0:
            empty_cols.append(i)

    for i, row in enumerate(galaxy):
        cols = empty_cols[0:]
        row = list(row)
        string = ''
        j = 0
        while j < len(row) - 1:
            if j in cols:
                row.insert(j, '.')
                cols = [x+1 for x in cols]
                j += 1

            j += 1

        row = string.join(row)
        galaxy[i] = row

    return galaxy


def check_rows(galaxy):
    expanded_galaxy = galaxy[0:]
    r = 0

    for line in galaxy:
        galaxy_count = 0

        for c in line:
            if c == '#':
                galaxy_count += 1

        if galaxy_count == 0:
            expanded_galaxy.insert(r, line)
            r += 1

        r += 1

    return expanded_galaxy


def def_value():
    return 0


def main(filename):
    data = open(filename).read()
    lines = data.split('\n')

    expanded_galaxy = check_cols(lines)
    expanded_galaxy = check_rows(expanded_galaxy)

    print(expanded_galaxy)

    galaxies = []
    for r, line in enumerate(expanded_galaxy):
        for c, thing in enumerate(line):
            if thing == '#':
                galaxies.append((r, c))

    pairs = list(combinations(galaxies, 2))

    print(galaxies)

    total = 0
    for pair in pairs:
        shortest_distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

        print(f'The shortest distance between {pair} is {shortest_distance}')
        total += shortest_distance

    print(total)


if __name__ == '__main__':
    main('11-input.txt')
