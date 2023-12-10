n, s, k = map(int, input().split())
ans = 0
for i in range(n):
    p, q = map(int, input().split())
    ans += p * q
if ans >= s:
    ans += 0
else:
    ans += k
print(ans)
