from collections import Counter
N = int(input())
A = list(map(int,input().split()))
L = Counter(A)
anss = {}
sum_ans = sum([i*(i-1)//2 for i in L.values() if i >= 2])
for k,v in L.items():
    anss[k] = sum_ans - (v*(v-1)//2) + ((v-1)*(v-2)//2)
for i in A:
    print(anss[i])
