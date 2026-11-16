# 8-Puzzle using A* (no imports). h = misplaced tiles. Node = [f, g, state, parent, move]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
start = [8, 1, 3, 4, 0, 2, 7, 6, 5]   # change this to try other puzzles
def misplaced(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count = count + 1
    return count
def is_solvable(state):               # solvable only if inversions are even
    inv = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inv = inv + 1
    return inv % 2 == 0
def neighbors(state):
    result = []
    for b in range(9):                # find the blank
        if state[b] == 0:
            break
    moves = [(-3, "Up", b > 2), (3, "Down", b < 6),
             (-1, "Left", b % 3 > 0), (1, "Right", b % 3 < 2)]
    for step, name, allowed in moves:
        if allowed:
            new = state[:]
            new[b] = new[b + step]    # tile slides into the blank
            new[b + step] = 0
            result.append([new, name])
    return result
def a_star(start):
    open_list = [[misplaced(start), 0, start, None, ""]]
    closed = []
    while open_list:
        best = 0                      # pick node with smallest f
        for i in range(len(open_list)):
            if open_list[i][0] < open_list[best][0]:
                best = i
        node = open_list.pop(best)
        if node[2] == goal:
            return node
        closed.append(node[2])
        for new_state, move in neighbors(node[2]):
            if new_state not in closed:
                g = node[1] + 1
                open_list.append([g + misplaced(new_state), g, new_state, node, move])
    return None
if not is_solvable(start):
    print("This puzzle cannot be solved.")
else:
    node = a_star(start)
    print("Solved in", node[1], "moves\n")
    path = []
    while node is not None:           # walk back through parents
        path.insert(0, node)
        node = node[3]
    for step in range(len(path)):
        print("Step", step, path[step][4])
        s = path[step][2]
        print(s[0], s[1], s[2], "\n" + str(s[3]), s[4], s[5], "\n" + str(s[6]), s[7], s[8], "\n")