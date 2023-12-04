M, D = map(int, input().split())
y, m, d = map(int, input().split())

# Day
if D != d:
    ans_d = d + 1
else:
    ans_d = 1

# Month
if D != d:
    ans_m = m
elif M != m:
    ans_m = m + 1
else:
    ans_m = 1

# Year
if D == d and M == m:
    ans_y = y + 1
else:
    ans_y = y


print(ans_y, ans_m, ans_d)
