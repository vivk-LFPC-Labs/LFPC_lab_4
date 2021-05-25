def get_first(prod):
    first = dict()
    for (key, value) in prod.items():
        first[key] = dict()
        for result in value:
            to_add = list()
            if result[0] == result[0].lower() or result[0] == '-':
                to_add.append((result[0], result))
            else:
                to_add = get_first_from_string(result[0], prod)

            if to_add is None or to_add == []:
                continue

            if len(to_add) != 0:
                for (letter, r) in to_add:
                    first[key][letter] = result
            elif to_add[0][0] == '_':
                raise Exception('FAILED to compute FIRST(' + key + '). Grammar is left-recursive.')

    return first


def get_first_from_string(c, prod):
    value = prod[c]
    found = list()
    for i in range(0, len(value)):
        result = value[i]
        if result[0] == result[0].lower() or result[0] == '-':
            found.append((result[0], result))
        else:
            if c == result[0]:
                prod[c][i] = prod[c][i][1:]

            new_found = get_first_from_string(result[0], prod)
            for (letter, r) in new_found:
                found.append((letter, r))

    return found
