A,B = map(int,input().split())
ans = 0
tap = 1
while True:
    if tap>=B:
        break
    tap += (A-1)
    ans += 1
print(ans)
