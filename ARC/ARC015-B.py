N = int(input())
ans = [0] * 6
for i in range(N):
    saiko,saite = map(float,input().split())
    if saiko >= 35:
        ans[0] += 1
    if 30 <= saiko < 35:
        ans[1] += 1
    if 25 <= saiko < 30:
        ans[2] += 1
    if saite >= 25:
        ans[3] += 1
    if saite < 0 and saiko >= 0:
        ans[4] += 1
    if saiko < 0:
        ans[5] += 1
print(" ".join([str(i) for i in ans]))
