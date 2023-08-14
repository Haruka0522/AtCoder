import numpy as np
n, d = map(int, input().split())
s_array = np.array([list(input()) for i in range(n)])
p_status = False
tmp_days = 0
max_days = 0
for i in range(d):
    if "x" not in s_array[:, i]:
        p_status = True
        tmp_days += 1
    else:
        if p_status:
            max_days = max(tmp_days, max_days)
        p_status = False
        tmp_days = 0
if p_status:
    max_days = max(tmp_days, max_days)
print(max_days)
