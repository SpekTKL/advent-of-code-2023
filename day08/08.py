import math


def create_map(data):
    new_map = dict()
    lines = data.split('\n')

    for line in lines:
        temp = line.split('=')
        key = temp[0].strip()
        values = tuple(temp[1].strip()[1:-1].split(', '))

        new_map[key] = values

    return new_map


def traverse_map(my_map, instructions):
    key = 'AAA'
    index = 0
    count = 0

    while key != 'ZZZ':
        instruction = instructions[index]
        if instruction == 'L':
            key = my_map[key][0]
        if instruction == 'R':
            key = my_map[key][1]

        count += 1

        if index == len(instructions) - 1:
            index = 0
        else:
            index += 1

    return count


def traverse_map_from_key(my_map, instructions, key):
    index = 0
    count = 0

    while not key.endswith('Z'):
        instruction = instructions[index]
        if instruction == 'L':
            key = my_map[key][0]
        if instruction == 'R':
            key = my_map[key][1]

        count += 1

        if index == len(instructions) - 1:
            index = 0
        else:
            index += 1

    return count


def get_instructions(data):
    return list(data.strip())


def get_starting_keys(data):
    keys = []
    lines = data.split('\n')

    for line in lines:
        key = line.split('=')[0].strip()
        if key[-1] == 'A':
            keys.append(key)

    return keys


def part1(data):
    instructions = get_instructions(data[0])
    new_map = create_map(data[1])

    no_of_steps = traverse_map(new_map, instructions)
    print(f'The number of steps to ZZZ are {no_of_steps}')


def part2(data):
    instructions = get_instructions(data[0])
    new_map = create_map(data[1])
    starting_keys = get_starting_keys(data[1])

    steps_list = []
    for key in starting_keys:
        steps_list.append(traverse_map_from_key(new_map, instructions, key))

    least_possible_steps = math.lcm(*steps_list)
    print(f'The minimum number of steps required for part 2 are {least_possible_steps}')


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()
        temp = data.split('\n\n')
        part1(temp)
        part2(temp)


if __name__ == '__main__':
    main('08-input.txt')
