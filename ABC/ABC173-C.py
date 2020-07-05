import numpy as np
import itertools
H, W, K = map(int, input().split())
table = np.array([list(input()) for i in range(H)])
#table = np.vstack((table, np.zeros((1, W), int)))
#table = np.hstack((table, np.zeros((H + 1, 1), int)))
print(table)
count_black = np.count_nonzero(table == "#")
ans = 0
for h in range(H + 1):
    for w in range(W + 1):
        c_h = itertools.combinations(range(H), h)
        c_w = itertools.combinations(range(W), w)
        for
        black_i = np.count_nonzero(table[i_1:i_2, :] == "#")
        black_j = np.count_nonzero(table[:, j_1:j_2] == "#")
         black_ij = np.count_nonzero(table[i_1:i_2, j_1:j_2] == "#")
          k_tmp = count_black - black_i - black_j + black_ij
           if k_tmp == K:
                ans += 1
            print()

print(ans)
