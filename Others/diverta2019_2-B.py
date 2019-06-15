#自力のWA回答　大会はこれにて断念
import collections

N = int(input())
if N == 1:
    print(1)
    exit()

x_list = []
y_list = []

for i in range(N):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
    
p_list = [x_list[i] - x_list[i+1] for i in range(N-1)]
q_list = [y_list[i] - y_list[i+1] for i in range(N-1)]

pq_list = sorted([(p_list[i],q_list[i]) for i in range(N-1)],reverse=True)

pq_qty = collections.Counter(pq_list).most_common()[0][1]

print(N-pq_qty)


