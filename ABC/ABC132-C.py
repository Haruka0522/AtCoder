N = int(input())
d_list = list(map(int,input().split()))
d_list.sort()
print(d_list[N//2]-d_list[N//2-1])
