n = int(input())
a_list = list(map(int, input().split()))
ans = 0
max_a = 0
for i in range(n):
    if i == 0:
        max_a = a_list[i]
        ans += 0
    else:
        diff = max_a - a_list[i]
        if diff <= 0:
            ans += 0
            max_a = a_list[i]
        else:
            ans += abs(diff)
print(ans)
