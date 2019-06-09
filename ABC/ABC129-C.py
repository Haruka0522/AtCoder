#大会中には解けませんでした。

N,M = map(int,input().split())

def fib(n):
    f = ((1 + 5**0.5) / 2)**n / 5**0.5 + 0.5
    return int(f)

ans = fib(N)

b = int(input())
nozoku = fib(b)

for i in range(M-1):
    a = int(input())
    if a-b == 1:
        print(0)
        exit()
    nozoku = nozoku*(fib(a-b))
nozoku = nozoku*(fib(N-b))
ans -= nozoku
print(ans%1000000007)
