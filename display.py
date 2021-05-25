def print_productions(joined_productions):
    count = 1
    for (key, value) in joined_productions.items():
        for result in value:
            print(str(count) + '.', key + '->' + result)
            count += 1


def print_first_follow(data):
    for x in data:
        print(x, '- ', end='')
        for y in data[x]:
            print(y, end=',')
        print()


def print_pt(table, terminals):
    print(end='    ')
    for t in terminals:
        print(t, '   ', end='')
    print()
    for x in table.keys():
        print(x, end='   ')
        for y in terminals:
            if y in table[x].keys():
                print(table[x][y], ' ' * (5 - len(table[x][y])), sep='', end='')
            else:
                print('     ', end='')
        print()
