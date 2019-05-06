N = int(input())
ans = -1
NG = 0
A = list(map(int, input().split()))
while (NG == 0):
    for i in range(N):
        if (A[i] % 2 != 0):
            NG = 1
        A[i] = A[i] // 2
    ans += 1
print(ans)
