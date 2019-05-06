N = int(input())
A = list(map(int, input().split()))
ans = 0
if (sum(A) % N != 0):
    print(-1)
else:
    junin = int(sum(A) / N)
    for i in range(N):
        for j in range(1, N + 1):
            if (len(A[i:j]) == 0):
                break
            if (sum(A[i:j]) != junin * len(A[i:j])):
                ans += 1
    print(ans)
