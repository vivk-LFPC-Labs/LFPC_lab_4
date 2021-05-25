import json

import buffer
from Tree import DisplayTree
from display import print_productions, print_first_follow, print_pt
from get_first import get_first
from get_follow import get_follow
from f_parser import parse as parsing
from parsing_table import build_parsing_table


def run(P, start, VN, VT, parse):
    buffer.word = str(parse)

    buffer.stack.append((start, 0))

    print('Initial productions:')
    print_productions(P)

    print('\nFISRT:')
    first = get_first(P)
    print_first_follow(first)

    print('\nFOLLOW:')
    follow = get_follow(P, start)
    print_first_follow(follow)

    print('\nParsing table:')
    parsing_table = build_parsing_table(first, follow)
    print_pt(parsing_table, VT)

    (tree, status) = parsing(parsing_table, follow, 1)

    print('\nString:', parse)
    if status:
        x = DisplayTree()
        x.print_tree(tree)
    else:
        print("Parsing failed!")


if __name__ == "__main__":
    with open('gram.json') as json_file:
        grammar = json.load(json_file)

    VN = grammar['VN']
    VT = grammar['VT']
    P = grammar['P']
    start_symbol = grammar['start_symbol']

    parse = 'aaaacadeebbb'

    run(P, start_symbol, VN, VT, parse)
