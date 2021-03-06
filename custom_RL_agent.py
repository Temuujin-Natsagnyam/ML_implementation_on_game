import time
import random
import math
savefile = "mapsave.txt"  # savefile

dummy_weights = [[random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)],
                [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)],
                [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)],
                [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)],
                [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)],
                [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,100)],
                 ]
def terrain(map):
    #ctr = 0
    #for xc in range(4):
        #for yc in range(4):
            #chance = random.randint(1,25)
            #if chance == 6 or chance == 3 or chance == 1:
                #map[xc][yc] = "G"
                #ctr += 1

    map[0][0] = "X"
    map[0][1] = "X"
    map[0][2] = "X"
    map[0][3] = "X"
    map[0][4] = "X"
    map[0][5] = "X"
    map[1][0] = "X"
    map[2][0] = "X"
    map[3][0] = "X"
    map[4][0] = "X"
    map[5][0] = "X"
    map[1][5] = "X"
    map[2][5] = "X"
    map[3][5] = "X"
    map[4][5] = "X"
    map[5][5] = "X"
    map[5][1] = "X"
    map[5][2] = "X"
    map[5][3] = "X"
    map[5][4] = "X"

    map[3][2]=  "X"
    map[3][1]= "X"
    map[3][3]= "X"
    map[4][1]= "G"
    return map
def seperate(word):  # function that takes a word and makes it a list of all the characters inside the word
    result = []
    for l in word:
        result.append(l)
    return result
def makemap(x, y):
    map = []  # declare empty array/ will be big list
    print("\n")  # new line for cleaner GUI
    # the array becomes a 2D array aka small lists inside a big list
    for z in range(0, y):  # y decides how many lists will go inside the big list, will be the vertical value of grid
        map.append(["O"] * x)  # x decides how long one small list will be, will be horizontal value for grid
    map = terrain(map)
    return map  # RETURNS ARRAY, not the map, but the array of it
def save(map):  # function used to save the progress onto an external txt file
    mapp = []  # declare empty array
    for row in range(len(map)):  # row iterates as each row of the grid // or each small list inside big list
        mapp.append(''.join(str(v) for v in map[row]))  # composite shortcut: it has a second loop
        # it joins all the little lists inside the big list, so the 2d array becomes a normal list
        mapp.append('\n')  # add a newline at each row orelse everything becomes one big line
    savemap = ''.join(str(a) for a in mapp)  # joins the remaining list
    fo = open(savefile, "w")  # open savefile and nuke it
    fo.write(savemap)  # save it
    fo.close()  # close it
def findxchar(row, char):  # func to locate character and returns its x coordinate position
    row = seperate(row)  # turns the row into a list of all its characters
    for xc in range(len(row)):  # checks every element in row // linear search
        if row[xc] == char:  # check
            return xc  # x coordinate of char
def locate(y, x, char):  # finds both coordinates of character from save file
    x = int(x)  # int type
    fo = open(savefile, "r+")  # open save file
    ctr = 0
    while ctr <= int(y):
        row = fo.read((x + 1)).strip()  # takes a line out of the save file
        tempx = findxchar(row, char)    # checks if that row contains character
        if tempx is not None:      # if it does have character that means it does not return None
            xc = tempx # in which case tempx is the x coordinate or xc
            yc = ctr# the ctr is also used to keep track of what line we are on, so the moment we find char we can say ctr is the vertical value
        ctr += 1
    fo.close()
    return xc, yc
def readnshow(x,y):
    x = int(x)  # int type
    fo = open(savefile, "r+")  # open save file
    ctr = 0
    while ctr <= int(y):
        row = fo.read((x + 1)).strip() # read a line from the save file
        print(row)     # print that
        ctr += 1   # each iteration goes to the next line
    fo.close()
def blind_agent():
    options = ["w","a","s","d"]
    choice = random.choice(options)
    return choice
def pythagor(px,py):
    base = 1 - px
    height = 4 - py
    hypo = math.sqrt(base**2 + height**2)
    hypo = int(hypo)
    return hypo
def want_goal(px,py):   #G is at [4][1])
    py = int(py)
    px = int(px)

    up_closeness = int(dummy_weights[py - 1][px]) - 3 * (pythagor(px, py - 1))
    dummy_weights[py - 1][px] = up_closeness

    down_closeness = int(dummy_weights[py + 1][px]) - 3 * (pythagor(px, py + 1))
    dummy_weights[py + 1][px] = down_closeness

    right_closeness = int(dummy_weights[py][px+1]) - 3* (pythagor(px+1, py))
    dummy_weights[py][px+1] = right_closeness

    left_closeness = int(dummy_weights[py][px - 1]) - 3 * (pythagor(px-1, py))
    dummy_weights[py][px-1] = left_closeness
def undo(px,py):
    py = int(py)
    px = int(px)

    gg = 2.4
    up_closeness = int(dummy_weights[py - 1][px]) + gg * (pythagor(px, py - 1))
    dummy_weights[py - 1][px] = up_closeness

    down_closeness = int(dummy_weights[py + 1][px]) + gg * (pythagor(px, py + 1))
    dummy_weights[py + 1][px] = down_closeness

    right_closeness = int(dummy_weights[py][px+1]) + gg * (pythagor(px+1, py))
    dummy_weights[py][px+1] = right_closeness

    left_closeness = int(dummy_weights[py][px - 1]) + gg * (pythagor(px-1, py))
    dummy_weights[py][px-1] = left_closeness
def less_dumb_agent(x,y,char,flag):
    px, py = locate(y, x, char)

    want_goal(px,py)

    #vision
    up = dummy_weights[py-1][px]      #[y][x]
    down = dummy_weights[py+1][px]
    right = dummy_weights[py][px+1]
    left = dummy_weights[py][px-1]

    dic = {up:"w",down:"s",right:"d",left:"a"}
    #choice
    if flag == 0:
        best = max(up,down,right,left)
        #print("fk")
    if flag == 1:
        best = max(up,down,right)
        #print("check: not go left")
    if flag == 2:
        best = max(up,down,left)
        #print("check: not go right")
    if flag == 3:
        best=max(down,right,left)
        #print("check: not go up")
    if flag == 4:
        #print("check: not go down")
        best = max(up, right, left)

    decision = dic[best]


    undo(px,py)



    print ("Selected move (Look below for change): ",decision)
    return decision
def move(map, x, y, char, world,flag):

    direction = less_dumb_agent(x,y,char,flag)
    print("\n")
    #time.sleep(1)
    px, py = locate(y, x, char)
    #print("coordinates of x",px,py)
    map[py][px] = "O"  # map[y][x]


    if direction == "d":
        px = px + 1
        flag = 1
    elif direction == "a":
        px = px - 1
        flag=2
    elif direction == "s":
        py = py + 1
        flag = 3
    elif direction == "w":
        py = py - 1
        flag = 4



    if map[py][px] == "X":                                      #detects collision with X
        print("Weight of move made that resulted crash: ",dummy_weights[py][px] )
        print(dummy_weights)
        temp = dummy_weights[py][px]
        temp -= 5                       #punishment
        dummy_weights[py][px] = temp
        print("New Value of weight: ",dummy_weights[py][px] )
        print(dummy_weights)
        if flag == 1:
            px = px - 1
        if flag == 2:
            px = px + 1
        if flag == 3:
            py = py -1
        if flag == 4:
            py = py + 1
    if px == 6:         #bound
        px=5
    if py == 6:
        py=5
    if px == -1:
        px =0
    if py == -1:
        py =0
    if map[py][px] == "G":                                      #detects goal
        print(("You've reached the goal"))
        brk = True
        return flag,brk
    map[py][px] = char
    save(map)#
    brk = False
    return  flag,brk
def main():
    x=int(6)
    y=int(6)
    char = ("P")
    world = int(1)
    map = makemap(x, y)
    map[1][1] = char  # map[y][x]
    save(map)
    readnshow(x,y)
    flag = 0
    ctr = 0
    while True:
        flag , brk= move(map, x, y, char, world,flag)
        readnshow(x,y)
        ctr+=1
        if brk is True:
            print("\nNumber of moves until goal reached: ",ctr)
            break
    return ctr
ctr1 = main()
ctr2 = main()
ctr3 = main()
ctr4 = main()
print(dummy_weights)
print("\nGen1: ",ctr1," Gen2: ",ctr2," Gen3: ",ctr3," GEN4:",ctr4)
