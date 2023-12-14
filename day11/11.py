from itertools import combinations


def get_empty_cols(universe):
    empty_cols = []
    row_length = len(universe[0])

    for i in range(row_length):
        galaxy_count = 0
        for row in universe:
            if row[i] == '#':
                galaxy_count += 1

        if galaxy_count == 0:
            empty_cols.append(i)

    return empty_cols


def get_empty_rows(galaxy):
    empty_rows = []

    for i, line in enumerate(galaxy):
        galaxy_count = 0
        for c in line:
            if c == '#':
                galaxy_count += 1

        if galaxy_count == 0:
            empty_rows.append(i)

    return empty_rows


def calculate_empty_cols_crossed(galaxy, empty_cols):
    return len([x for x in empty_cols if galaxy[1] > x])


def calculate_empty_rows_crossed(galaxy, empty_rows):
    return len([x for x in empty_rows if galaxy[0] > x])


def get_new_position(galaxy, empty_rows, empty_cols):
    cols_crossed = calculate_empty_cols_crossed(galaxy, empty_cols)
    rows_crossed = calculate_empty_rows_crossed(galaxy, empty_rows)

    return galaxy[0] + (999999 * rows_crossed), galaxy[1] + (999999 * cols_crossed)


def check_cols(galaxy):
    empty_cols = get_empty_cols(galaxy)

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


def get_galaxies(universe):
    galaxies = []
    for r, line in enumerate(universe):
        for c, thing in enumerate(line):
            if thing == '#':
                galaxies.append((r, c))

    return galaxies


def get_shortest_distance(pair):
    return abs(pair[0][0] - pair [1][0]) + abs(pair[0][1] - pair[1][1])


def part1(lines):
    expanded_galaxy = check_cols(lines)
    expanded_galaxy = check_rows(expanded_galaxy)

    galaxies = get_galaxies(expanded_galaxy)

    pairs = list(combinations(galaxies, 2))
    print(len(pairs))

    total = 0
    for pair in pairs:
        total += get_shortest_distance(pair)

    print(f'The sum of all shortest lengths is {total}')


def part2(lines):
    galaxies = get_galaxies(lines)
    empty_cols = get_empty_cols(lines)
    empty_rows = get_empty_rows(lines)

    for i, galaxy in enumerate(galaxies):
        galaxies[i] = get_new_position(galaxy, empty_rows, empty_cols)

    pairs = list(combinations(galaxies, 2))
    print(len(pairs))

    total = 0
    for pair in pairs:
        total += get_shortest_distance(pair)

    print(f'The sum of distances in the larger universe is {total}')


def main(filename):
    data = open(filename).read()
    lines = data.split('\n')
    part1(lines[0:])
    part2(lines[0:])


if __name__ == '__main__':
    main('11-input.txt')
