def get_difference_list(numbers):
    new_list = list()
    index = 0

    while index < len(numbers) - 1:
        new_list.append(int(numbers[index+1]) - int(numbers[index]))
        index += 1

    return new_list


def part1(lines):
    last_numbers = []

    for line in lines:
        num_and_diff = []
        numbers = [int(x) for x in line.split()]
        num_and_diff.append(numbers)

        difference_list = get_difference_list(numbers)
        num_and_diff.append(difference_list)

        while difference_list.count(0) != len(difference_list):
            difference_list = get_difference_list(difference_list)
            num_and_diff.append(difference_list)

        index = len(num_and_diff) - 1
        while index > 0:
            updated_value = num_and_diff[index-1][-1] + num_and_diff[index][-1]
            num_and_diff[index-1].append(updated_value)
            index -= 1

        last_numbers.append(num_and_diff[0][-1])

    return last_numbers


def part2(lines):
    first_numbers = []

    for line in lines:
        num_and_diff = []
        numbers = [int(x) for x in line.split()]
        num_and_diff.append(numbers)

        difference_list = get_difference_list(numbers)
        num_and_diff.append(difference_list)

        while difference_list.count(0) != len(difference_list):
            difference_list = get_difference_list(difference_list)
            num_and_diff.append(difference_list)

        index = len(num_and_diff) - 1
        while index > 0:
            updated_value = num_and_diff[index - 1][0] - num_and_diff[index][0]
            num_and_diff[index - 1].insert(0, updated_value)
            index -= 1

        first_numbers.append(num_and_diff[0][0])

    return first_numbers


def main(filename):
    with open(filename, 'r') as file:
        data = file.read()
        lines = data.split('\n')

        result1 = part1(lines)
        print(f'The total of all the predicted values is {sum(result1)}')
        result2 = part2(lines)
        print(f'The total sum of all the extrapolated values is {sum(result2)}')


if __name__ == '__main__':
    main('09-input.txt')