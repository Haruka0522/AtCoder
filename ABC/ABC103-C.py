N = int(input())
a_li = list(map(int,input().split()))

print(sum([a-1 for a in a_li]))

