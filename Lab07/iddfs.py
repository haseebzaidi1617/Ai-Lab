# Task B: Find goal node G using IDDFS, starting from A.

class Graph:
    def __init__(self):
        # Store each node and its connected neighbours.
        self.adj = {}

    def addEdge(self, u, v):
        # Create an empty list if node is not present.
        if u not in self.adj:
            self.adj[u] = []

        if v not in self.adj:
            self.adj[v] = []

        # Add neighbour to the starting node.
        self.adj[u].append(v)

    # Depth Limited Search function.
    def DLS(self, start, goal, depth_limit):

        # Store nodes with their depth and path.
        stack = [(start, 0, [start])]

        # Store traversal order.
        visited = []

        # Continue until stack becomes empty.
        while stack:

            # Remove the last added item.
            vertex, depth, path = stack.pop()

            # Record the visited node.
            visited.append(vertex)

            # Check whether goal is found.
            if vertex == goal:
                return path, visited

            # Stop at the depth limit.
            if depth >= depth_limit:
                continue

            # Get neighbours of current node.
            neighbours = self.adj.get(vertex, [])

            # Start from the last neighbour.
            i = len(neighbours) - 1

            # Add neighbours in reverse order.
            while i >= 0:

                neighbour = neighbours[i]

                # Avoid cycles in the current path.
                if neighbour not in path:
                    stack.append(
                        (neighbour, depth + 1, path + [neighbour])
                    )

                i -= 1

        return None, visited

    # Iterative Deepening Search function.
    def IDDFS(self, start, goal, max_depth):

        # Increase depth limit from 0 to max_depth.
        for limit in range(max_depth + 1):

            print(f"\nDepth Limit: {limit}")

            # Call DLS for the current depth limit.
            path, visited = self.DLS(start, goal, limit)

            # Display nodes visited in this iteration.
            print("Traversal:", " -> ".join(visited))

            # Check whether goal is found.
            if path is not None:

                print(f"Goal node '{goal}' reached successfully!")
                print("Final Path:", " -> ".join(path))
                return

        print(f"\nGoal node '{goal}' not found!")


# Main driver code: Create graph and run IDDFS.

if __name__ == "__main__":

    g = Graph()

    # Connect A to B, F, D and E.
    g.addEdge('A', 'B')
    g.addEdge('A', 'F')
    g.addEdge('A', 'D')
    g.addEdge('A', 'E')

    # Connect B to K and J.
    g.addEdge('B', 'K')
    g.addEdge('B', 'J')

    # Connect K to N and M.
    g.addEdge('K', 'N')
    g.addEdge('K', 'M')

    # Connect D to goal node G.
    g.addEdge('D', 'G')

    # Connect E to C, H and I.
    g.addEdge('E', 'C')
    g.addEdge('E', 'H')
    g.addEdge('E', 'I')

    # Connect I to L.
    g.addEdge('I', 'L')

    # Run IDDFS with maximum depth 3.
    g.IDDFS('A', 'G', 3)