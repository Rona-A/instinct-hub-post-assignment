#Description: This program runs a connect-four game on a 2D grid, it looks at if there are 4 x's either horizontally or vertically.

def connect_four(the_grid, player_symbol):
    # check for horizontal matches
    for row in the_grid:
        #print(row)
        for y in range(len(row) - 3):
            if row[y] == player_symbol and row[y + 1] == player_symbol and row[y + 2] == player_symbol and row[y + 3] == player_symbol:
                return True
    #the_grid[this is changimg][]
    # check for vertical matches
    for col in range(len(the_grid)): #check each colomn index
        for x in range(len(the_grid[0]) - 3): #check each row index
            if the_grid[x][col] == player_symbol and the_grid[x + 1][col] == player_symbol and the_grid[x + 2][col] == player_symbol and the_grid[x + 3][col] == player_symbol:
                return True
    return False

if __name__ == '__main__':
    rows = int(input('How many rows will be entered? '))
    grid = []
    for x in range(rows):
        new_row = []
        new_line = input()
        for char in new_line:
            new_row.append(char)
        grid.append(new_row)
    print(connect_four(grid, 'x'))
