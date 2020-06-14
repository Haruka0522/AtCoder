X,N = map(int,input().split())
p_li = set(map(int,input().split()))
p = set(range(-200,200))
kouho = p - p_li
ans = 10000
sa_min = 1000000
for i in sorted(list(kouho)):
    sa = abs(X-i)
    if sa_min > sa:
        ans = i
        sa_min = sa
print(ans)
