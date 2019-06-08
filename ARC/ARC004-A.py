import math
N = int(input())
zahyo = [list(map(int,input().split())) for i in range(N)]
distance = []
for i in range(N):
    for j in range(N):
        A = zahyo[i]
        B = zahyo[j]
        distance.append(math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2))
print(max(distance))
