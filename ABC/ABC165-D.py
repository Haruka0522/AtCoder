from math import floor
A,B,N = map(int,input().split())
#"""
if N < B:
    print(max(floor(A*N/B)-A*floor(N/B),floor(A*(N-1)/B)-A*floor((N-1)/B)))
else:
    print(max(floor(A*N/B)-A*floor(N/B),floor(A*B/B)-A*floor(B/B),floor(A*(B-1)/B)-A*floor((B-1)/B),floor(A*(N-1)/B)-A*floor((N-1)/B),floor(A*(B+1)/B)-A*floor((B+1)/B)))
#"""
#for x in range(100):
#    print(x,floor(A*x/B)-A*floor(x/B))
