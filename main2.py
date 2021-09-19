import sys

with open(sys.argv[1]) as file:
    ilosc = file.readline()
    wagi = file.readline()
    kol1 = file.readline()
    kol2 = file.readline()

wagi_lista = wagi.split(" ")
kol1_lista = kol1.split(" ")
kol2_lista = kol2.split(" ")
zwazone_slonie = {}
for slon in range(int(wagi_lista)):
