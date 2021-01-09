

string1, x, y = input().split()
# string1, x, y = "CAT", 1, 2
x = int(x)
y = int(y)
string2 = input()
# string2 = "BALL"
common_char = [i for i in string1 if i in string2][0]
index1 = string1.index(common_char) # x_of constant
index2 = string2.index(common_char) # y - index2 is y_of



star_grid = [['*']*10 for _ in range(10)]

def update(string, start, mode='v'):
    l = len(string)
    x, y = start 
    x_end = x+l 

    if mode == 'v':
        for i in range(x, x_end):
            star_grid[i][y] = string[i-x]
    
    else:
        y_end = y+l 
        for i in range(y, y_end):
            star_grid[x][i] = string[i-y]

    return star_grid

print_star_grid = lambda : print('\n'.join([''.join(i) for i in star_grid]))
update(string1, (x, y))

x_of = index1 + x
y_of = y - index2 

update(string2, (x_of, y_of), 'h')

print_star_grid()

