x, y = input().split()
x, y = int(x), int(y)

posX, posY, dir = input().split()
posX = int(posX)
posY = int(posY)

num_moves = len(input())

r_final = lambda ps_x, ps_y : 0<=ps_x<x and 0<=ps_y<y 

if dir == "N":
    final = (posX, posY - num_moves)

elif dir == "S":
    final = (posX, posY + num_moves)

elif dir == "E":
    final = (posX - num_moves, posY)

elif dir == "W":
    final = (posX + num_moves, posY)

if r_final(*final): print(final[0], final[1], dir)
else:
    print(posX, posY, dir)
    print("Out of Boundary")
    

