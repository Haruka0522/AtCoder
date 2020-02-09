N,K = map(int,input().split())
h_list = [int(input()) for i in range(N)]
h_list.sort()
result = []
print(min([h_list[i+K-1]-h_list[i] for i in range(N-K+1)]))
