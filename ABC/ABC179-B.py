n = int(input())
d = [set(input().split()) for i in range(n)]
for i in range(n-2):
    if len(d[i]) == len(d[i+1]) == len(d[i+2]) == 1:
        print("Yes")
        exit()
print("No")
