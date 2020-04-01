N = int(input())
checked = [0]*10**5
ans = 0
for i in range(N):
    A = int(input())
    if checked[A-1] == 1:
        ans += 1
    else:
        checked[A-1] = 1
print(ans)
