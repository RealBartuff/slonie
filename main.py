
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

with open("zadanie_B/slo1.in") as file:
    N = file.readline()
    wagi = list(map(int, file.readline().split(" ")))
    a = Permutation(list(map(int, file.readline().split(" "))))
    b = Permutation(list(map(int, file.readline().split(" "))))
