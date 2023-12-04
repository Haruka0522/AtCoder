N, x = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.sort()
ans = 0

for i in range(N):
    if i == N-1:
        if x == a_list[i]:
            ans += 1
    elif x >= a_list[i]:
        x -= a_list[i]
        ans += 1
    else:
        break
print(ans)
