
field = list( ['1', '2', '3', '4', '5', '6', '7', '8', '9'] )

def show_field(field):
    print("{} | {} | {}".format(field[0], field[1], field[2]))
    print("===========")
    print("{} | {} | {}".format(field[3], field[4], field[5]))
    print("===========")
    print("{} | {} | {}".format(field[6], field[7], field[8]))


def get_x():
    val = input("Player 1, enter the number: ")
    return int(val)-1

def get_o():
    val = input("Player 2, enter the number: ")
    return int(val)-1

def player_x():
    print('Player 1 is won!')

def player_o():
    print('Player 2 is won!')

def check_field(field):

    #check lines
    if (len(set(field[:3]))) == 1:
        player_x() if field[0] == 'X' else player_o()
        return True
    if (len(set(field[3:6]))) == 1:
        player_x() if field[0] == 'X' else player_o()
        return True
    if (len(set(field[6:]))) == 1:
        player_x() if field[0] == 'X' else player_o()
        return True

    #check columns
    if (len(set((field[0], field[3], field[6])))) == 1:
        player_x() if field[0] == 'X' else player_o()
        return True
    if (len(set((field[1], field[4], field[7])))) == 1:
        player_x() if field[0] == 'X' else player_o()
        return True
    if (len(set((field[2], field[5], field[8])))) == 1:
        player_x() if field[0] == 'X' else player_o()
        return True
    
    #check diagonals
    if (len(set((field[0], field[4], field[8])))) == 1:
        player_x() if field[0] == 'X' else player_o()
        return True
    if (len(set((field[2], field[4], field[6])))) == 1:
        player_x() if field[0] == 'X' else player_o()
        return True


    return False

end_game = False
i = 0
while end_game == False:
    show_field(field)

    if i % 2:
        pos = get_o()
        field[pos] = '0'
    else:
        pos = get_x()
        field[pos] = 'X'

    if check_field(field):
        end_game = True

    i += 1

    if i==9 and end_game is not True:
        print('Нічия!')
        end_game = True

