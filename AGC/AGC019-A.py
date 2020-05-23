Q,H,S,D = map(int,input().split())
ans = 0
N = int(input())
costs = sorted([(Q*8,0.25),(H*4,0.5),(S*2,1.0),(D,2.0)])
for cost,v in costs:
    if N < v:
        continue
    if v == 0.25:
        cost //= 8
    elif v == 0.5:
        cost //= 4
    elif v == 1.0:
        cost //= 2
    else:
        cost //= 1
    a = N // v
    if (a*v) % v != 0:
        a -= 1
    N -= v * a
    ans += cost * a
    if N == 0:
        break
print(int(ans))
