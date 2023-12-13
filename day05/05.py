def is_even(num):
    return num % 2 == 0


def get_seeds(line):
    seeds = []
    ranges = []
    seeds_and_ranges = line.split(':')[1].split(' ')[1:]

    for index, sr in enumerate(seeds_and_ranges):
        if is_even(index):
            seeds.append(int(sr))
            continue

        ranges.append(int(sr))

    return seeds, ranges


def get_lines(section):
    return section.split('\n')[1:]


def in_range(key, values):
    return values[1] <= key < values[1] + values[2]


def get_mapped_value(key, line_values):
    diff = key - line_values[1]
    return line_values[0] + diff


def get_values(line):
    line_elems = line.split(' ')
    destination_range_start = int(line_elems[0])
    source_range_start = int(line_elems[1])
    range_length = int(line_elems[2])

    return destination_range_start, source_range_start, range_length


def check_section(key, section):
    lines = get_lines(section)
    for line in lines:
        values = get_values(line)
        if in_range(key, values):
            return get_mapped_value(key, values)

    return key


def main():
    with open('input-05.txt', mode='r', encoding='utf-8') as f:
        text = f.read()
        sections = text.split('\n\n')

        seeds_and_ranges = get_seeds(sections[0])
        seeds = seeds_and_ranges[0]
        ranges = seeds_and_ranges[1]

        print(seeds)
        print(ranges)

        locations = []

        for index, seed in enumerate(seeds):
            seed = int(seed)
            max_seed = seed + ranges[index]
            while seed < max_seed:
                print(seed)
                key = seed
                for i in range(1, 8):
                    key = check_section(key, sections[i])

                locations.append(key)
                seed += 1

        print(f"The lowest location number is {min(locations)}")


main()
