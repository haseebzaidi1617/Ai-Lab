
graph = {
    1: [2, 7, 8],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [9, 12],
    9: [10, 11],
    10: [],
    11: [],
    12: []
}

# Print Graph
def print_graph(G):
    for node in G:
        print(f"{node} -> {G[node]}")


print_graph(graph)


# Iterative DFS
def DFS_iterative(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            for w in reversed(graph[node]):
                if w not in visited:
                    stack.append(w)


print("\nIterative DFS:")
DFS_iterative(graph, 1)
