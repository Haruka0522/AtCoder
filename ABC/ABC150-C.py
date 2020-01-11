import itertools

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

permutation_list = list(itertools.permutations(range(1,N+1),N))
a = permutation_list.index(P)
b = permutation_list.index(Q)
print(abs(a-b))
