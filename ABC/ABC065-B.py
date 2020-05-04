N = int(input())
a_li = [int(input()) for i in range(N)]
a_li.insert(0,-1)
osu = 1
for i in range(N):
    ima = a_li[osu]
    if ima == 2:
        print(i+1)
        exit()
    osu = ima
print(-1)
