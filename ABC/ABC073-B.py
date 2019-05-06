ans = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    ans += b - a + 1
print(ans)
