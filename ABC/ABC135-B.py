N = int(input())
P1 = list(map(int,input().split()))
P2 = sorted(P1)
different = 0
for i in range(N):
    if P1[i] != P2[i]:
        different += 1
if different <= 2:
    print("YES")
else:
    print("NO")
