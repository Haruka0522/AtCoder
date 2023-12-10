n, m = map(int, input().split())
s = input()
useable_m = m
useable_l = 0
have_m = m
have_l = 0
for i in range(n):
    schedule = s[i]
    if schedule == "0":
        useable_m = have_m
        useable_l = have_l
    elif schedule == "1":
        if useable_m >= 1:
            useable_m -= 1
        elif useable_l >= 1:
            useable_l -= 1
        else:
            have_l += 1
    elif schedule == "2":
        if useable_l >= 1:
            useable_l -= 1
        else:
            have_l += 1
print(have_l)
