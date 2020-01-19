H = int(input())
W = int(input())
N = int(input())

for i in range(min(H,W)):
    if max(H,W)*(i+1)>=N:
        print(i+1)
        exit()
