def get_follow(prod, start):
    follow = search_follow(prod, start, 0)

    for k in prod.keys():
        if not k in follow.keys():
            follow[k] = ['$']

    return follow


def search_follow(prod, word, i):
    follow = dict()
    for (idx, symbol) in enumerate(word):
        if symbol == symbol.upper():
            for result in prod[symbol]:
                if result != '-':
                    last_nt = word[-1:]
                    if last_nt == last_nt.upper() and i != 0:
                        if not last_nt in follow.keys():
                            follow[last_nt] = list()

                        follow[last_nt].append('$')

                    new_word = word[:idx] + result + word[idx + 1:]
                    new_prod = dict()
                    for (k, v) in prod.items():
                        new_prod[k] = list()
                        for y in v:
                            if y != result:
                                new_prod[k].append(y)

                    returned = search_follow(new_prod, new_word, i + 1)
                    for (k, v) in returned.items():
                        for y in v:
                            if not k in follow.keys():
                                follow[k] = list()

                            if not y in follow[k]:
                                follow[k].append(y)

    for (idx, symbol) in enumerate(word):
        if idx + 1 < len(word):
            if symbol == symbol.upper() and word[idx + 1] == word[idx + 1].lower():
                if not symbol in follow.keys():
                    follow[symbol] = list()

                if not word[idx + 1] in follow[symbol]:
                    follow[symbol].append(word[idx + 1])

    return follow
