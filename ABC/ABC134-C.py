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

#解説を見て
A = [int(input()) for i in range(int(input()))]
first = max(A)
second = sorted(A)[-2]
for i in A:
    if i == first:
        print(second)
    else:
        print(first)
