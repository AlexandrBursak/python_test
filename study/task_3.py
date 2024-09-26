maze = [
    ['#', '.', '.', '.', '.'],
    ['.', '.', '#', '#', 'S'],
    ['.', '#', '#', '#', '#'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', 'E']
]

max_i, max_j = len(maze[0]), len(maze)

def show_maze():
    print(maze[0])
    print(maze[1])
    print(maze[2])
    print(maze[3])
    print(maze[4])

def find_start():
    i=0
    start_point = None
    while start_point is None and i < max_i:
        try:
            start_point = maze[i].index('S')
        except ValueError:
            start_point = None

        if start_point is None:
            i += 1
        
        print('Should we go to new loop: i, start_point ', i, start_point)
    
    return i, start_point

def check_new_position(pos_i, pos_j):
    print('Check positions: ', pos_i+1, pos_j+1)
    if maze[pos_i][pos_j] == 'E':
        raise Exception('We found the finish')

    if maze[pos_i][pos_j] == '.':
        print('Path: ', pos_i+1, pos_j+1)
        maze[pos_i][pos_j] = 'x'
        return True
    return False


def find_new_step(pos_i, pos_j):
    # look around
    show_maze()

    print('Start Check positions: ', pos_i, pos_j)

    # up
    if pos_j - 1 >= 0:
        new_pos_j = pos_j - 1
        new_pos_i = pos_i

        if (check_new_position(new_pos_i, new_pos_j)):
            find_new_step(new_pos_i, new_pos_j)
    
    # right
    if pos_i + 1 < max_i:
        new_pos_i = pos_i + 1
        new_pos_j = pos_j

        if (check_new_position(new_pos_i, new_pos_j)):
            find_new_step(new_pos_i, new_pos_j)
    
    # down
    if pos_j + 1 < max_j:
        new_pos_j = pos_j + 1
        new_pos_i = pos_i

        if (check_new_position(new_pos_i, new_pos_j)):
            find_new_step(new_pos_i, new_pos_j)
    
    # left
    if pos_i - 1 >= 0:
        new_pos_i = pos_i - 1
        new_pos_j = pos_j

        if (check_new_position(new_pos_i, new_pos_j)):
            find_new_step(new_pos_i, new_pos_j)
    
    raise Exception('We can\'t find the finish')


i, j = find_start()
print('Start point i,j: ', i+1, j+1)


try:
    find_new_step(i, j)
except Exception as m:
    print(m)

