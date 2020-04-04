N,K = map(int,input().split())
a = N // K
print(min(abs(N-(K*a)),abs(N-(K*(a+1)))))
