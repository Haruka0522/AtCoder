N = int(input())
prices = [int(input()) for i in range(N)]
prices_uni = list(set(prices))
prices_uni.sort(reverse=True)
print(prices_uni[1])
