
f = open("/Users/nicolgotzova/Documents/Advent of Code/Day_2.txt", encoding="utf-8")
complete_paper = f.read()
f.close()
lines = complete_paper.split('\n')

counter = 0
celkovy_objem = 0
for line in lines:
    counter = counter + 1
    values_list = line.split("x")
    sirka = int(values_list [0])
    vyska = int(values_list [1])
    delka = int(values_list [2])
    #print (f"Výška je:{sirka}, sirka je: {vyska}, delka je: {delka}")
     
    present = (2*sirka*vyska) + (2*vyska*delka) + (2*delka*sirka)
    extra_paper = min (sirka*vyska, vyska*delka, delka*sirka)
    total = present + extra_paper
    #objem_1 = sirka * vyska * delka
    
    celkovy_objem = celkovy_objem + total
    """if counter == 5:
        break"""
     
print (f"Celkovy objem je: {celkovy_objem}")

#sorted(values_list)[:2] 

