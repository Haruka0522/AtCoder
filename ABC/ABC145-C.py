import itertools
from math import sqrt

N = int(input())
zahyo = []
kyori_ichiran = []
for i in range(N):
    x,y = map(int,input().split())
    zahyo.append((x,y))
junban_ichiran = list(itertools.permutations(range(N),N))
for i in range(len(junban_ichiran)):
    junban = junban_ichiran[i]
    kyori = 0
    for j in range(len(junban)-1):
        kyori += sqrt((zahyo[junban[j]][0]-zahyo[junban[j+1]][0])**2 + (zahyo[junban[j]][1]-zahyo[junban[j+1]][1])**2)
    kyori_ichiran.append(kyori)
print(sum(kyori_ichiran)/len(kyori_ichiran))
