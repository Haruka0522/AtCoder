N,K = map(int,input().split())
def base_10_to_n(X,N):
    if (int(X/N)):
        return base_10_to_n(int(X/N),N)+str(X%N)
    return str(X%N)
print(len(base_10_to_n(N,K)))
