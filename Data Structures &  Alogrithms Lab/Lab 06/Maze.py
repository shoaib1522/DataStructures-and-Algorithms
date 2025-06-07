def solve_maze(maze):
    stack = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "P":
                stack.append((i, j))
    while len(stack) != 0:
        i, j = stack[-1]
        if maze[i][j] == "T":
            return "Solved", stack
        if is_valid_move(maze, i - 1, j):
            stack.append((i - 1, j))
            maze[i][j] = "*" 
        elif is_valid_move(maze, i + 1, j):
            stack.append((i + 1, j))
            maze[i][j] = "*"
        elif is_valid_move(maze, i, j - 1):
            stack.append((i, j - 1))
            maze[i][j] = "*"
        elif is_valid_move(maze, i, j + 1):
            stack.append((i, j + 1))
            maze[i][j] = "*"
        else:
            stack.pop()
            maze[i][j] = "X" 
    return "Unsolved", None
def is_valid_move(maze, i, j):
    if 0 <= i < len(maze) and 0 <= j < len(maze[0]):
        if maze[i][j] == " " or maze[i][j] == "T":
            return True
    return False
def main():
    maze = [
        [" ", "*", " ", "*", " ", " "],
        [" ", "*", " ", "*", " ", " "],
        ["P", " ", " ", " ", "*", " "],
        ["*", " ", "*", "*", "*", " "],
        [" ", " ", " ", " ", "*", "T"],
        ["*", " ", " ", " ", " ", " "]
    ]
    status, path = solve_maze(maze)
    print(status)
    if status == "Solved":
        print("Path:", path)
    maze = [
        [" ", "*", " ", "*", " ", " "],
        [" ", "*", " ", "*", " ", " "],
        ["P", " ", " ", " ", "*", " "],
        ["*", " ", "*", "*", "*", " "],
        [" ", " ", " ", " ", "*", "T"],
        ["*", " ", " ", " ", " ", "*"]
    ]
    status, path = solve_maze(maze)
    print(status)
    if status == "Solved":
        print("Path:", path)
main()
