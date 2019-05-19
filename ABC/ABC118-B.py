N,M = map(int,input().split())
list_a = []
ans = 0
for i in range(N):
    list_a.append(list(map(int,input().split())))

for i in range(1,M+1):
    count = 0
    for f_food in list_a:
        f_food[0] = -1
        if(i in f_food):
            count += 1
    if(count == len(list_a)):
            ans += 1
print(ans)


