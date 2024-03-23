n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = (1+k)*k//2
checked = set()
for i in a:
    if (i <= k) and (i not in checked):
        ans -= i
        checked.add(i)
print(ans)
