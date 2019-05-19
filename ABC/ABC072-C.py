#TLE解答
'''
N = int(input())
A = list(map(int,input().split()))
ans = []
for X in range(min(A),max(A)+1):
    count = 0
    for i in A:
        if(abs(i-X) <= 1):
            count += 1
    ans.append(count)
print(max(ans))
'''

#解説を見て
import collections
N = int(input())
A = list(map(int,input().split()))
list_A = []
for i in  range(N):
    list_A.append(A[i])
    list_A.append(A[i]+1)
    list_A.append(A[i]-1)
print(collections.Counter(list_A).most_common()[0][1])
