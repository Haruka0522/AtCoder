N = int(input())
a_list = list(map(int,input().split()))
ans = 0
for i,a in enumerate(a_list):
    if a_list[a-1] == i+1:
        ans += 1
print(ans//2)
