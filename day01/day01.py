nums = []


def updated_line(line):
    line = line.replace('one', 'one1one')
    line = line.replace('two', 'two2two')
    line = line.replace('three', 'three3three')
    line = line.replace('four', 'four4four')
    line = line.replace('five', 'five5five')
    line = line.replace('six', 'six6six')
    line = line.replace('seven', 'seven7seven')
    line = line.replace('eight', 'eight8eight')
    line = line.replace('nine', 'nine9nine')

    return line


def main():
    with open('input-day1-01', mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        for text in lines:
            strnum = ''
            text = updated_line(text)
            for char in text:
                if char.isdigit():
                    strnum += char
            nums.append(int(strnum[0] + strnum[-1]))

        print(sum(nums))


if __name__ == '__main__':
    main()