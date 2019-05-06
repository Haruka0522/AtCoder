N = int(input())
a = list(map(int,input().split()))
max_a = max(a)
a.remove(max_a)
if(max_a < sum(a)):
    print("Yes")
else:
    print("No")