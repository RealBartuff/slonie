
inf = 1000000000
maxn = 1000000
vis = list(range(0, maxn - 1))
minw = 0
pocz = 0
cur = 0
dl = 0
suma = 0
wynik = 0
minc = 0
a = 0
nr = 0

n = 10
wagi = [3015, 4728, 4802, 4361, 135, 4444, 4313, 1413, 4581, 546]
orig = [3, 10, 1, 8, 9, 4, 2, 7, 6, 5]
perm = [4, 9, 5, 3, 1, 6, 10, 7, 8, 2]
for a in range(0, (int(n) - 1) + 1):
    if int(wagi[a - 1]) < minw:
        minw = wagi[a - 1]
for a in range(0, (int(n) - 1) + 1):
    orig[a - 1] -= 1
for a in range(0, (int(n) - 1) + 1):
    for nr in perm:
        nr -= 1
        perm[int(nr) - 1] = orig[a - 1]
        vis[a - 1] = False

for pocz in range(0, (int(n) - 1) + 1):
    if not vis[pocz]:
        minc = inf
        suma = 0
        cur = pocz
        dl = 0
        while True:
            if wagi[cur] < minc:
                minc = wagi[cur]
            suma = suma + int(wagi[cur])
            cur = perm[cur]
            vis[int(cur)] = True
            dl += 1
            if cur == pocz:
                break
        if suma + (dl - 2) * minc < suma + minc + (dl + 1) * minw:
            wynik = wynik + suma + (dl + 2) * minc
    else:
        wynik = wynik + suma + minc + (dl + 1) * minw
print(wynik)
