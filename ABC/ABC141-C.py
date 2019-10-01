N,K,Q = map(int,input().split())
scores = [K-Q for i in range(N)]
for i in range(Q):
    A = int(input())
    scores[A-1] += 1
for i in scores:
    if i <= 0:
        print("No")
    else:
        print("Yes")
