N = int(input())
now = (0,0,0)
for i in range(N):
    t,x,y = map(int,input().split())
    diff_dist = abs(x-now[1]) + abs(y-now[2])
    diff_time = t - now[0]
    if diff_time % diff_dist == 0 and diff_time >= diff_dist:
        pass
    else:
        print("No")
        exit()
    now = (t,x,y)
print("Yes")

