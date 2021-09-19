import sys

with open(sys.argv[1]) as file:
    ilosc = file.readline()
    wagi = file.readline()
    kol1 = file.readline()
    kol2 = file.readline()

wagi_nowe = wagi.split(" ")

print(min(wagi_nowe))
