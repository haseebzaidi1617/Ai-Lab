# Task 2: Alpha-Beta Pruning using a Graph class

INF = 999999


class Graph:
    def __init__(self):
        self.children = {}      # node -> list of child nodes
        self.value = {}         # leaf node -> value

    def add_node(self, parent, child):
        if parent not in self.children:
            self.children[parent] = []
        self.children[parent].append(child)

    def add_leaf(self, node, value):
        self.value[node] = value


def alpha_beta(g, node, is_max, alpha, beta):
    if node not in g.children:          # leaf node
        return g.value[node]

    if is_max:
        best = -INF
        for child in g.children[node]:
            val = alpha_beta(g, child, False, alpha, beta)
            if val > best:
                best = val
            if best > alpha:
                alpha = best
            if beta <= alpha:           # prune
                break
        return best
    else:
        best = INF
        for child in g.children[node]:
            val = alpha_beta(g, child, True, alpha, beta)
            if val < best:
                best = val
            if best < beta:
                beta = best
            if beta <= alpha:           # prune
                break
        return best


# Build the tree from the manual
g = Graph()
g.add_node('A', 'B'); g.add_node('A', 'C')
g.add_node('B', 'D'); g.add_node('B', 'E')
g.add_node('C', 'F'); g.add_node('C', 'G')
g.add_node('D', 'D1'); g.add_node('D', 'D2')
g.add_node('E', 'E1'); g.add_node('E', 'E2')
g.add_node('F', 'F1'); g.add_node('F', 'F2')
g.add_node('G', 'G1'); g.add_node('G', 'G2')

g.add_leaf('D1', 3); g.add_leaf('D2', 5)
g.add_leaf('E1', 6); g.add_leaf('E2', 9)
g.add_leaf('F1', 1); g.add_leaf('F2', 2)
g.add_leaf('G1', 0); g.add_leaf('G2', -1)

print("Optimal value:", alpha_beta(g, 'A', True, -INF, INF))   # Output: 5