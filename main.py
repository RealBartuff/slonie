
INF = 1000000000
MAXN = 1000000

wagi = [0 for _ in range(MAXN)]
orig = [0 for _ in range(MAXN)] # orig[i] = kto stal na pozycji i
perm = [0 for _ in range(MAXN)] # slon i ma wyladowac na pozycji slonia perm[i]
vis = [False for _ in range(MAXN)] # nalezy do juz zbadanego cyklu

minw = INF # minimalna waga

@staticmethod
def main(args):
    rd = java.io.BufferedReader(java.io.InputStreamReader(System.in))
    n = 0
    try:
        input = java.util.StringTokenizer(rd.readLine())
        N = int(input.nextToken())
        input = java.util.StringTokenizer(rd.readLine())
        a = 0
        while a < n:
            wagi[a] = int(input.nextToken())
            minw = min(minw, wagi[a])
            a += 1
        input = java.util.StringTokenizer(rd.readLine())
        a = 0
        while a < n:
            orig[a] = int(input.nextToken())-1
            a += 1
        input = java.util.StringTokenizer(rd.readLine())
        a = 0
        while a < n:
            perm[int(input.nextToken())-1] = orig[a]
            a += 1
    except java.io.IOException as e:
        pass

    wynik = 0
    pocz = 0
    while pocz < n:
        if not vis[pocz]:
            minc = INF # minimalna waga w cyklu
            suma = 0 # suma wag w cyklu
            cur = pocz
            dl = 0 # dlugosc cyklu
            while True:
                minc = min(minc, wagi[cur])
                suma += wagi[cur]
                cur = perm[cur]
                vis[cur] = True
                dl += 1
                if cur == pocz:
                    break
            wynik += min(suma+(dl-2)*int(minc), suma+minc+(dl+1)*int(minw))
        pocz += 1
    print(wynik)