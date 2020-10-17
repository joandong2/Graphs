
def earliest_ancestor(ancestors, starting_node):
    # Make empty graph
    graph = {}
    for edge in ancestors:
        ancestor, child = edge[0], edge[1]
        if ancestor in graph:
            graph[ancestor].add(child)
        else:
            graph[ancestor] = set()
            graph[ancestor].add(child)

    stack = []
    stack.append(starting_node)

    while len(stack) > 0:
        current_node = stack.pop()
        #print('curr', current_node)
        for k, v in graph.items():
            #print(f'{k} {v}')
            # if starting_node not in v:
            #     return -1

            if current_node in v:
                print('parent', k)
                stack.append(k)

    if current_node == starting_node:
        return -1

    return current_node

    # '''
    #    10
    #  /
    # 1   2   4  11
    #  \ /   / \ /
    #   3   5   8
    #    \ / \   \
    #     6   7   9
    # '''

    ############## {1: {3}, 2: {3}, 3: {6}, 5: {6, 7}, 4: {8, 5}, 8: {9}, 11: {8}, 10: {1}}


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
#                   (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 10))
