S = list(input())
A_index = S.index("A")
S_gyaku = [i for i in S[::-1]]
Z_index = len(S) - S_gyaku.index("Z")
print(Z_index-A_index)
