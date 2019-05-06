N = int(input())
prices = []
for i in range(N):
    prices.append(int(input()))
max_price = max(prices)
prices.remove(max_price)
print(int(sum(prices)+(max_price/2)))