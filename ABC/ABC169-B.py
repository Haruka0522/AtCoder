N = int(input())
A_li = sorted(list(map(int,input().split())))
ans = 1
for i in A_li:
    ans *= i
    if ans > 10**18:
        print(-1)
        exit()
print(ans)

