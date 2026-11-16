# Task 3: 8 Puzzle using A* Search

class PuzzleState:

    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.f = 0

    # Find the empty space (0)
    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    # Generate possible next moves
    def generate_children(self):

        children = []
        x, y = self.find_zero()

        moves = [
            (x-1, y, "Up"),
            (x+1, y, "Down"),
            (x, y-1, "Left"),
            (x, y+1, "Right")
        ]

        for nx, ny, move in moves:

            if 0 <= nx < 3 and 0 <= ny < 3:

                # Copy the board
                new_board = [row[:] for row in self.board]

                # Swap empty space with the tile
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]

                children.append(PuzzleState(new_board, self, move, self.depth + 1))

        return children


# Count misplaced tiles
def heuristic(board, goal):

    count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                count += 1

    return count


# A* Search Algorithm
def a_star_search(start, goal):

    open_list = [PuzzleState(start)]
    closed_list = []

    open_list[0].f = heuristic(start, goal)

    while open_list:

        # Select state with minimum f value
        current = min(open_list, key=lambda s: s.f)
        open_list.remove(current)

        # Check if goal is reached
        if current.board == goal:

            path = []

            while current.parent:
                path.append(current.move)
                current = current.parent

            return path[::-1]

        closed_list.append(current.board)

        # Generate and check child states
        for child in current.generate_children():

            if child.board not in closed_list:

                child.f = child.depth + heuristic(child.board, goal)
                open_list.append(child)

    return None


# Initial State
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Run A* Search
solution = a_star_search(start, goal)

if solution is not None:
    print("Solution Found!")
    print("Total Moves:", len(solution))
    print("Moves:", solution)
else:
    print("No Solution Found!")