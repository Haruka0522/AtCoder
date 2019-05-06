N = int(input())
ans = 0
for i in range(1,N+1):
    yakusu_count = 0
    if(i%2 == 1):
        for j in range(1,i+1):
            if(i%j == 0):
                yakusu_count += 1
        if(yakusu_count == 8):
            ans += 1
print(ans)