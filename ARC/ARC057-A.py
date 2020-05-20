A,K = map(int,input().split())
i = 0
if K == 0:
    print(2*10**12-A)
    exit()
while A < 2*10**12:
    i += 1
    A += (1 + K*A)
print(i)
