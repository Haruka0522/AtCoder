N, M = map(int, input().split())
students = []
checkpoint = []
for i in range(N):
    students.append(list(map(int, input().split())))
for j in range(M):
    checkpoint.append(list(map(int, input().split())))
for k in students:
    a, b = k[0], k[1]
    distance = []
    for l in checkpoint:
        c, d = l[0], l[1]
        distance.append(abs(a - c) + abs(b - d))
    print(distance.index(min(distance))+1)
