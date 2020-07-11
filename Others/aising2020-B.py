N = int(input())
a_li = list(map(int,input().split()))
ans = 0
for idx,a in enumerate(a_li):
    if a % 2 == 1 and (idx+1) % 2 == 1:
        ans += 1
print(ans)
