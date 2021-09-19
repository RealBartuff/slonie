import sys


class Slon:
    def __init__(self):
        self.INF = 1000000000
        self.MAXN = 1000000
        self.wagi = [0 for _ in range(self.MAXN)]
        self.orig = [0 for _ in range(self.MAXN)] # orig[i] = kto stal na pozycji i
        self.perm = [0 for _ in range(self.MAXN)] # slon i ma wyladowac na pozycji slonia perm[i]
        self.vis = [False for _ in range(self.MAXN)] # nalezy do juz zbadanego cyklu
        self.minw = self.INF # minimalna waga

    def main(self):
        with open(sys.argv[1]) as file:
            try:
                line1 = file.readline()
                line1_lst = line1.split(" ")
                for i in line1_lst:
                    n = int(i)
                    a = 0
                    while a < n:
                        line2 = file.readline()
                        line2_lst = line2.split(" ")
                        for k in line2_lst:
                            k = self.wagi[a]
                            self.minw = min(self.minw, k)
                            a += 1
                        a = 0
                        while a < n:
                            line3 = file.readline()
                            line3_lst = line3.split(" ")
                            for o in line3_lst:
                                self.orig[a] = int(o)-1
                                a += 1
                            a = 0
                            while a < n:
                                line4 = file.readline()
                                line4_lst = line4.split(" ")
                                for e in line4_lst:
                                    self.perm[int(e)-1] = self.orig[a]
                                    a += 1
            except IOError:
                pass

            wynik = 0
            pocz = 0
            while pocz < n:
                if not self.vis[pocz]:
                    minc = self.INF # minimalna waga w cyklu
                    suma = 0 # suma wag w cyklu
                    cur = pocz
                    dl = 0 # dlugosc cyklu
                    while True:
                        minc = min(minc, self.wagi[cur])
                        suma += self.wagi[cur]
                        cur = self.perm[cur]
                        self.vis[cur] = True
                        dl += 1
                        if cur == pocz:
                            break
                    wynik += min(suma+(dl-2)*int(minc), suma+minc+(dl+1)*int(self.minw))
                pocz += 1
            print(wynik)


Slon().main()
