N = int(input())
max_count = 0
ans = 1
for i in range(1,N+1):
    count = 0
    num = i
    while(1):
        if(num%2 == 0):
            num = int(num/2)
            count += 1
        else:
            break
    if(count > max_count):
        max_count = count
        ans = i
print(ans)