def part2(race_durations, record_distances):
    duration = ''
    distance = ''

    for i, d in enumerate(race_durations):
        duration += d
        distance += record_distances[i]

    duration = int(duration)
    distance = int(distance)
    false_count = 0

    for speed in range(duration):
        if not speed * (duration - speed) > distance:
            false_count += 1
        else:
            break

    print(f'The total number of ways to win the race the race is {duration - (false_count * 2) + 1}')


def part1(race_durations, record_distances):
    multiply_values = 1

    for index, duration in enumerate(race_durations):
        total_wins = 0
        for speed in range(int(duration) + 1):
            if speed * (int(duration) - speed) > int(record_distances[index]):
                total_wins += 1

        multiply_values *= total_wins

    print(f'The multiple of all the ways to win is {multiply_values}')


if __name__ == '__main__':
    with open('input-06.txt', 'r') as file:
        lines = file.readlines()
        race_duration = lines[0].split(':')[1].strip().split()
        record_distance = lines[1].split(':')[1].strip().split()

    part1(race_duration, record_distance)
    part2(race_duration, record_distance)
