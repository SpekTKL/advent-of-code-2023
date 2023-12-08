POSSIBLE_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

possible_games = set()


def get_color(color):
    if color[-1] == ',' or color[-1] == ';' or color[-1] == '\n':
        return color[0:-1]

    return color


def get_game_id(game_text):
    strnum = game_text.split(' ')[1]
    return int(strnum)


def parse_elements(element):
    num_col = []
    element = element.strip()
    num_col.append(int(element.split(' ')[0]))
    num_col.append(element.split(' ')[1])

    return num_col


def is_game_possible(game):
    elements = game.split(',')
    for element in elements:
        parts = parse_elements(element)
        if parts[0] > POSSIBLE_CUBES.get(parts[1]):
            return False

    return True


def get_power(game):
    min_of_colours = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for subgame in game:
        elements = subgame.split(',')
        for element in elements:
            parts = parse_elements(element)
            if parts[0] > min_of_colours.get(parts[1]):
                min_of_colours[parts[1]] = parts[0]

    return min_of_colours.get('red') * min_of_colours.get('green') * min_of_colours.get('blue')


def main():
    try:
        with open('input-day02-01.txt', mode='r', encoding='utf-8') as file:
            games = file.read().split('\n')
            total_power = 0
            for game in games:
                is_possible = True
                game_id = game.split(':')
                subgames = game_id[1].split(';')
                game_id = get_game_id(game_id[0])

                total_power += get_power(subgames)

                for subgame in subgames:
                    if not is_game_possible(subgame):
                        is_possible = False

                if is_possible:
                    possible_games.add(game_id)

    except FileNotFoundError:
        print("File not found")

    print(total_power)


if __name__ == '__main__':
    main()
    # print(sum(possible_games))
