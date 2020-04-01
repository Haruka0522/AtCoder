N = int(input())
a_li = sorted(list(map(int,input().split())),reverse=True)
Alice = sum(a_li[::2])
Bob = sum(a_li) - Alice
print(Alice - Bob)
