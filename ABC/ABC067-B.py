N,K = map(int,input().split())
l_li = list(map(int,input().split()))
l_li.sort(reverse=True)
print(sum(l_li[:K]))
