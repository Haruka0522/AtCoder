N = int(input())
A = list(input())
B = list(input())
C = list(input())
ans = 0
for i in range(N):
    abc = set([A[i],B[i],C[i]])
    ans += len(abc) - 1
print(ans)


