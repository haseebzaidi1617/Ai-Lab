
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost=1):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))

    def a_star_search(self, start, target, heuristic):

        open_set = []
        g_costs = {}
        closed_set = []
        path = []

        # Insert starting node
        open_set.append((heuristic[start], 0, start))
        g_costs[start] = 0

        while len(open_set) > 0:

            # Find node with smallest f value
            min_index = 0

            for i in range(1, len(open_set)):
                if open_set[i][0] < open_set[min_index][0]:
                    min_index = i

            # Remove minimum f value node
            f, g, current = open_set[min_index]
            open_set.pop(min_index)

            # Skip already explored nodes
            if current in closed_set:
                continue

            # Store explored node
            path.append(current)

            # Check goal
            if current == target:
                print("\nNode", target, "found using A* Search!")
                print("Total Cost:", g)
                print("Nodes Explored:", path)
                return True

            closed_set.append(current)

            # Explore neighbours
            for neighbor, cost in self.graph[current]:

                g_new = g + cost

                if neighbor not in g_costs or g_new < g_costs[neighbor]:

                    g_costs[neighbor] = g_new

                    f_new = g_new + heuristic[neighbor]

                    # Insert neighbour manually
                    open_set.append((f_new, g_new, neighbor))

        print("\nNode", target, "not found.")
        print("Nodes Explored:", path)

        return False

# Example Graph
g = Graph()

g.add_edge("A", "B", 1)
g.add_edge("A", "C", 3)
g.add_edge("B", "D", 1)
g.add_edge("B", "E", 3)
g.add_edge("C", "F", 1)
g.add_edge("E", "G", 1)
# Heuristic Values
heuristic = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 10,
    "E": 1,
    "F": 2,
    "G": 0
}
# Perform A* Search
g.a_star_search("A", "G", heuristic)
