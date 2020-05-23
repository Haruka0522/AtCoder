def pow(a,n):
    x = 1
    while n > 0:
        if n & 1:
            x *= a
        a *= a
        n >>= 1
        if x > 10**9:
            print("large")
            exit()
    return x
A,R,N = map(int,input().split())
S_n = A * pow(R,N-1)
if S_n > 10 ** 9:
    print("large")
else:
    print(int(S_n))
