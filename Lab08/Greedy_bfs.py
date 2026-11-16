
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        if v not in self.graph[u]:
            self.graph[u].append(v)

        if u not in self.graph[v]:
            self.graph[v].append(u)

    # Greedy Best First Search
    def greedy_search(self, start, target, heuristic):

        visited = set()
        pq = []
        path = []

        # Insert starting node manually
        pq.append((heuristic[start], start))
        visited.add(start)

        while len(pq) > 0:

            # Find node with smallest heuristic
            min_index = 0

            for i in range(1, len(pq)):
                if pq[i][0] < pq[min_index][0]:
                    min_index = i

            # Remove minimum priority node manually
            priority, current = pq[min_index]
            pq.pop(min_index)

            # Store explored node
            path.append(current)

            # Check goal
            if current == target:
                print("\nNode", target, "found using Greedy Search!")
                print("Nodes Explored:", path)
                return True

            # Explore neighbours
            for neighbor in self.graph[current]:

                if neighbor not in visited:

                    # Insert neighbour manually
                    pq.append((heuristic[neighbor], neighbor))
                    visited.add(neighbor)

        print("\nNode", target, "not found.")
        print("Nodes Explored:", path)
        return False


# Example Graph
g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("B", "E")
g.add_edge("C", "F")
g.add_edge("E", "G")


# Heuristic Values
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 10,
    'E': 1,
    'F': 2,
    'G': 0
}

# Perform Greedy Search
g.greedy_search('A', 'G', heuristic)
