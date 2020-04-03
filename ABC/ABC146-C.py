import bisect
A,B,X = map(int,input().split())
low = 0
high = 10**9
while low <= high:
    mid = (low + high) // 2
    kingaku = A * mid + B * len(str(mid))
    mae = (low,high)
    if kingaku < X:
        low = mid - 1
    elif kingaku > X:
        high = mid + 1
    else:
        print(mid)
        exit()
    if mae == (low,high):
        break
#print(low,high)
for i in range(high,low-1,-1):
    if A * i + B * len(str(i)) <= X:
        print(i)
        exit()
print(0)
