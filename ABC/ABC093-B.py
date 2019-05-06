"""
#TLE回答
A, B, K = map(int, input().split())
seisu = [i for i in range(A, B + 1)]
mitasu_seisu = []
for j in seisu[:K]:
    mitasu_seisu.append(j)
for k in seisu[-K:]:
    mitasu_seisu.append(k)
for l in sorted(list(set(mitasu_seisu))):
    print(l)
"""

A, B, K = map(int, input().split())
mitasu_seisu = []
for i in range(A, min(A + K, B)):
    mitasu_seisu.append(i)
for j in range(max(A, B - K + 1), B + 1):
    mitasu_seisu.append(j)
for k in sorted(set(mitasu_seisu)):
    print(k)
