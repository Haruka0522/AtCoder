num = list(map(int,input().split()))
if(5 in num and 7 in num and sum(num) == 17):
    print("YES")
else:
    print("NO")