# BFS implementation without built-in functions

class Graph:

    def __init__(self):
        self.graph = {
            0: [1, 4],
            1: [0, 4, 3, 2],
            2: [1, 3],
            3: [4, 1, 2],
            4: [0, 1, 3]
        }

    def bfs(self, start):

        visited = [False] * 5
        queue = [0] * 5

        front = 0
        rear = 0

        queue[rear] = start
        rear = rear + 1

        visited[start] = True

        while front < rear:

            node = queue[front]
            front = front + 1

            print(node, end=" ")

            for neighbour in self.graph[node]:

                if visited[neighbour] == False:

                    visited[neighbour] = True

                    queue[rear] = neighbour
                    rear = rear + 1


g = Graph()

print("BFS Traversal:")
g.bfs(0)