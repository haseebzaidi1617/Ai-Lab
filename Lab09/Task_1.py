# Task 1: Minimax using a Graph class

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


def minimax(g, node, is_max):
    if node not in g.children:          # leaf node
        return g.value[node]

    if is_max:
        best = -INF
        for child in g.children[node]:
            val = minimax(g, child, False)
            if val > best:
                best = val
        return best
    else:
        best = INF
        for child in g.children[node]:
            val = minimax(g, child, True)
            if val < best:
                best = val
        return best


# Build the tree from the manual
g = Graph()
g.add_node('A', 'B'); g.add_node('A', 'C')
g.add_node('B', 'D'); g.add_node('B', 'E')
g.add_node('C', 'F'); g.add_node('C', 'G')
g.add_node('D', 'H'); g.add_node('D', 'I')
g.add_node('E', 'J'); g.add_node('E', 'K')
g.add_node('F', 'L'); g.add_node('F', 'M')
g.add_node('G', 'N'); g.add_node('G', 'O')

g.add_leaf('H', -1); g.add_leaf('I', 4)
g.add_leaf('J', 2);  g.add_leaf('K', 6)
g.add_leaf('L', -3); g.add_leaf('M', -5)
g.add_leaf('N', 0);  g.add_leaf('O', 7)

print("Optimal value:", minimax(g, 'A', True))   # Output: 4