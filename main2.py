
inf = 1000000000
maxn = 1000000
perm = []
vis = []

minw = int()

a = int()
nr = int()
pocz = int()
cur = int()
dl = int()
wynik = 0
suma = int()
minc = int()

with open("zadanie_B/slo1.in") as file:
    n = file.readline()
    for a in range(0, (int(n) - 1) + 1):
        wagi = file.readline().split(" ")
        if int(wagi[a - 1]) < minw:
            minw = wagi[a - 1]
    for a in range(0, (int(n) - 1) + 1):
        orig = file.readline().split(" ")
        orig[a - 1] -= 1
    for a in range(0, (int(n) - 1) + 1):
        perm = file.readline().split(" ")
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
                if wagi[cur] < str(minc):
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
