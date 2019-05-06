# WA部分点100/200点回答
N, T = map(int, input().split())
A_list = list(map(int, input().split()))
ans = 0
for i in A_list:
    ans += i//T
print(ans)
