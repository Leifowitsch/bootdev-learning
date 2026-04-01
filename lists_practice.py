def ungerade_zahlen(liste):
    neue_liste = [zahl for zahl in liste if zahl%2 != 0]
    return neue_liste

Zahlen = [2,5,7,23,45,214,1,6]

print(ungerade_zahlen(Zahlen))