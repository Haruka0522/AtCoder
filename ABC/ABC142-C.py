'''TLE解法
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    if i != N-1:
        print(A.index(i+1)+1,end=" ")
    else:
        print(A.index(i+1)+1)
'''

N = int(input())
ans = [0 for i in range(N)]
for num,i in enumerate(list(map(int,input().split()))):
    ans[i-1] = num + 1
print(*ans)
