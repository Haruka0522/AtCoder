import math
N,D = map(int,input().split())
ans = 0
X_list = []
for a in range(N):
    X_list.append(list(map(int,input().split())))
for i in range(N):
    for j in range(i+1,N):
        rutononaka = 0
        for d in range(D):
            rutononaka += (X_list[i][d]-X_list[j][d])**2
        distance = math.sqrt(rutononaka)
        if distance == (distance//1):
            ans += 1
print(ans)


