N = int(input())
for n in range(1,N+1):
    f_n = 0
    xyz = [1,1,1]
    ans = 0
    while f_n < n:
        x,y,z = xyz
        f_n = x**2 + y**2 + z**2 + x*y + y*z + z*x
        if f_n == n:
            ans += 1
        xyz[xyz.index(min(xyz))] += 1
    f_n = 0

    if n == 6:
        print(ans)
    else:
        print(ans * 3)
