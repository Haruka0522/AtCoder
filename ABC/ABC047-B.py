W, H, N = map(int, input().split())
ans = 0
WH_list = [[0] * W, [0] * H]
for i in range(N):
    x, y, a = map(int, input().split())
    if (a == 1):
        for j in range(x):
            WH_list[0][j] = 1
    elif (a == 2):
        for j in range(x, W):
            WH_list[0][j] = 1
    elif (a == 3):
        for j in range(y):
            WH_list[1][j] = 1
    else:
        for j in range(y, H):
            WH_list[1][j] = 1
ans = WH_list[0].count(0) * WH_list[1].count(0)
print(ans)