def check_column(maze, column_now, row_now, last_way, start_position=False):
    if column_now < 0 or column_now >= len(maze):
        return []
    if start_position:
        return check_column(maze, column_now+1, row_now, last_way) + check_column(maze, column_now-1, row_now, last_way)
    if [column_now,row_now] in last_way:
        return []
    if maze[column_now][row_now] == "." or maze[column_now][row_now] == "E":
        return [[column_now,row_now]]
    return []

def check_row(maze, column_now, row_now, last_way, start_position=False):
    if row_now < 0 or row_now >= len(maze[0]):
        return []
    if start_position:
        return check_row(maze, column_now, row_now+1, last_way) + check_row(maze, column_now, row_now-1, last_way)
    if [column_now,row_now] in last_way:
        return []
    if maze[column_now][row_now] == "." or maze[column_now][row_now] == "E":
        return [[column_now,row_now]]
    return []

def search_way(entire_maze, column_now=0, row_now=0, last_way=[], exit_way=[]):
    posible_way = check_column(entire_maze, column_now, row_now, last_way, True) + check_row(entire_maze, column_now, row_now, last_way, True)
    last_way += posible_way
    for way in posible_way:
        if entire_maze[way[0]][way[1]] == "E":
            return exit_way + [way]
        else:
            result = search_way(entire_maze, way[0], way[1], last_way, exit_way + [way])
            if result:
                return result
    return []

def change_way(entire_maze, exit_way, start=0):
    if start >= len(exit_way) - 1:
        return
    word = entire_maze[exit_way[start][0]]
    left_word = word[0:exit_way[start][1]]
    right_word = word[exit_way[start][1] - len(word) + 1:]
    entire_maze[exit_way[start][0]] = left_word + "*" + right_word
    change_way(entire_maze, exit_way, start+1)

def result(entire_maze):
    print("Your maze:")
    print_way(entire_maze)
    result_way = search_way(entire_maze)
    if result_way:
        change_way(entire_maze, result_way)
        print("Solution found:")
        print_way(entire_maze)
    else:
        print("No solution found")

def print_way(entire_maze, start=0):
    if start >= len(entire_maze):
        return
    print(entire_maze[start])
    print_way(entire_maze, start+1)

print("Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.")
print("Separate each row with a comma (,).")
entire_maze = [maze for maze in input("Enter the maze: ").split(",")]
result(entire_maze)