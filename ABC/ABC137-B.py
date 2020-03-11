K,X = map(int,input().split())
ans = [str(i) for i in range(X-K+1,X+K)]
print(" ".join(ans))
