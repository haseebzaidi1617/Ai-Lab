# Task A: Find goal node G using DLS, starting from A.

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

    def DLS(self, start, goal, depth_limit):

        # Store nodes with their current depth and path.
        stack = [(start, 0, [start])]

        # Display starting node, goal and depth limit.
        print(f"DLS traversal from {start} to {goal}:")
        print(f"Depth Limit: {depth_limit}")

        # Continue until stack becomes empty.
        while stack:

            # Remove the last added item from stack.
            vertex, depth, path = stack.pop()

            # Display the current node.
            print(vertex, end=" ")

            # Check whether current node is the goal.
            if vertex == goal:
                print(f"\nGoal node '{goal}' reached successfully!")
                print("Final Path:", " -> ".join(path))
                return

            # Stop searching if depth limit is reached.
            if depth >= depth_limit:
                continue

            # Get neighbours of the current node.
            neighbours = self.adj.get(vertex, [])

            # Start from the last neighbour.
            i = len(neighbours) - 1

            # Add neighbours to stack in reverse order.
            while i >= 0:
                neighbour = neighbours[i]

                # Avoid visiting a node already in current path.
                if neighbour not in path:
                    stack.append(
                        (neighbour, depth + 1, path + [neighbour])
                    )

                i -= 1

        print(f"\nGoal node '{goal}' not found within depth limit!")


# Main driver code: Create graph and run DLS.

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

    # Run DLS with depth limit 2.
    g.DLS('A', 'G', 2)