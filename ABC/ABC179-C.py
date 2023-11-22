n = int(input())
ans = 0
for a in range(1, n):
    ans += n // a
    if n % a == 0:
        ans -= 1
print(ans)
