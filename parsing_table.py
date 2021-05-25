def build_parsing_table(first, follow):
    parsing_table = dict()
    for (key1, terminals) in first.items():
        parsing_table[key1] = dict()
        for (key2, production) in terminals.items():
            if key2 == '-':
                for symbol in follow[key1]:
                    parsing_table[key1][symbol] = '_'

            parsing_table[key1][key2] = production

    return parsing_table
