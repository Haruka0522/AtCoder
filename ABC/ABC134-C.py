'''TLE解答
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
for num,a in enumerate(A):
    del A[num]
    print(max(A))
    A.insert(num,a)
'''

'''TLE解答
A = [int(input()) for i in range(int(input()))]
for i in range(len(A)):
    print(max(A[:i]+A[i+1:]))
'''

