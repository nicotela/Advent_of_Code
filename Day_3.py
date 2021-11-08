"""f = open("/Users/nicolgotzova/Documents/Advent of Code/Test.txt", encoding="utf-8")
movements = f.read()
f.close()"""

movements = "^>v<"
position_x = 0
position_y = 0

grid = [[False]*4]*4
for znak in movements:
    print (znak)
    if znak == "^":
        position_y = position_y + 1 
    elif znak == ">":
        position_x = position_x + 1 
    elif znak == "v":
        position_y = position_y - 1
    elif znak == "<":
        position_x = position_x -1
    else:
        raise Exception (f"Neplatný znak: {znak}")
    print (f"Santa je na pozici {position_x}, {position_y}")