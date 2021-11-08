f = open("/Users/nicolgotzova/Documents/Advent of Code/Day_1.txt", encoding="utf-8")
floor = f.read()
f.close()

leva = floor.count ("(")
prava = floor.count (")")
print (leva-prava)