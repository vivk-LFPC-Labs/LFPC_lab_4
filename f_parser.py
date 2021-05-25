from Tree import Tree

import buffer


def parse(parsing_table, follow, i):
    node = Tree()
    if i > buffer.max_level:
        buffer.max_level = i

    stack_first = buffer.stack[-1:][0][0]

    if stack_first == stack_first.lower():
        node.data = buffer.word[0]
        node.level = i
        node.ls = stack_first
        del buffer.stack[-1:]
        buffer.word = buffer.word[1:]

        return node, True

    else:
        rules = parsing_table[stack_first]
        if buffer.word[0] in rules.keys():
            node.data = buffer.stack[-1:][0][0]
            node.level = i
            node.ls = buffer.stack[-1:][0][1]
            deleted = buffer.stack[-1:]
            del buffer.stack[-1:]

            if rules[buffer.word[0]] == '_':
                empty_node = Tree()
                empty_node.data = '-'
                empty_node.level = i + 1
                empty_node.ls = buffer.stack[-1:][0][1]

                node.children.append(empty_node)
                return node, True

            for (idx, c) in enumerate(reversed(rules[buffer.word[0]])):
                buffer.stack.append((c, len(rules[buffer.word[0]]) - idx + 1))

            for _ in rules[buffer.word[0]]:
                (new_children, state) = parse(parsing_table, follow, i + 1)
                if state:
                    node.children.append(new_children)
                else:
                    return node, False
        else:
            return node, False

    return node, True
