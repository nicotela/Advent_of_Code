
f = open("/Users/nicolgotzova/Documents/Advent of Code/Day_2.txt", encoding="utf-8")
complete_paper = f.read()
f.close()
lines = complete_paper.split('\n')

counter = 0
celkovy_objem = 0
for line in lines:
    counter = counter + 1
    values_list = line.split("x")
    #sorted_values_list = sorted(values_list)   #nevím proč, ale hodnoty mi to neseřadí od nejnižší 
    #sorted (vyska, sirka, delka)               #zase řve, že potřebuje jen jeden argument místo 3
    #min (values_list)                          #mi vyhodí jen nejnižší hodnotu. potřebuju poslední dvě hodnoty, co potřebuju
    sirka = int(sorted_values_list [0])
    vyska = int(sorted_values_list [1])
    delka = int(sorted_values_list [2])
    

    present = (sirka+sirka+vyska+vyska)
    extra_paper = (sirka*vyska*delka)
    total = present + extra_paper
    
    
    celkovy_objem = celkovy_objem + total
    """if counter == 5:
        break"""
     
print (f"Celkovy objem je: {celkovy_objem}")


