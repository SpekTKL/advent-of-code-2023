def create_map(data):
    new_map = dict()
    lines = data.split('\n')

    for line in lines:
        temp = line.split('=')
        key = temp[0].strip()
        values = tuple(temp[1].strip()[1:-1].split(', '))

        new_map[key] = values

    return new_map


def traverse_map(my_map, instructions, key='AAA'):
    index = 0
    count = 0

    while key != 'ZZZ':
        instruction = instructions[index]
        if instruction == 'L':
            key = my_map[key][0]
        if instruction == 'R':
            key = my_map[key][1]

        if index == len(instructions) - 1:
            index = 0
        else:
            index += 1

        count += 1

    return count


def get_instructions(data):
    return list(data.strip())


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()
        temp = data.split('\n\n')
        instructions = get_instructions(temp[0])
        new_map = create_map(temp[1])

        print(instructions)
        print(new_map)

        no_of_steps = traverse_map(new_map, instructions)
        print(f'The number of steps to ZZZ are {no_of_steps}')


if __name__ == '__main__':
    main('08-input.txt')
