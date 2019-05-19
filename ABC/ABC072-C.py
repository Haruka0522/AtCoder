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


