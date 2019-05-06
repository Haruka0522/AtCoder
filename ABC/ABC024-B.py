# 未解決問題
N, T = map(int, input().split())
ans = 0
mae = int(input())
for i in range(N-1):
    ima = int(input())
    if (ima - mae > T):
        ans += T
    else:
        ans += (ima - mae + T)
    mae = ima
print(ans)
