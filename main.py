
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

with open("zadanie_B/slo1.in") as file:
    N = int(file.readline())
    wagi = list(map(int, file.readline().split(" ")))
    a = list(map(int, file.readline().split(" ")))
    b = list(map(int, file.readline().split(" ")))
    slow = dict(zip(wagi, a))
