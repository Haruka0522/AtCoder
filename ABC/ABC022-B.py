N = int(input())
checked = []
ans = 0
for i in range(N):
    A = int(input())
    if A in checked:
        ans += 1
    checked.append(A)
print(ans)
