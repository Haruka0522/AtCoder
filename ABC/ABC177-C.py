n = int(input())
a_list = list(map(int, input().split()))
a_ruiseki = []
ruiseki = sum(a_list)
ans = 0
for i in range(n):
    ruiseki -= a_list[i]
    a_ruiseki.append(ruiseki)
for i in range(n - 1):
    ans += a_list[i] * a_ruiseki[i]
print(ans%(10**9+7))
