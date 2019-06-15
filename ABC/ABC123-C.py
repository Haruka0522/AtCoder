#解説AC
N = int(input())
min_cap = min([int(input()) for i in range(5)])
print(-(-N//min_cap)+4)
