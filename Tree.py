import numpy as np

import buffer


class Tree(object):
    def __init__(self):
        self.children = list()
        self.data = None
        self.level = None
        self.ls = None


class DisplayTree:
    def __init__(self):
        self.matrix = np.array([[' '] * (3 * buffer.max_level)] * (8 * buffer.max_level))
        self.i = 0

    def print_tree(self, node, file=None, _prefix="", _last=True):
        print(_prefix, "`- " if _last else "|- ", node.data, sep="", file=file)
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            self.print_tree(child, file, _prefix, _last)