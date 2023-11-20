s = input()
t = input()
s_l = len(s)
t_l = len(t)
max_match_count = 0
for i in range(s_l - t_l + 1):
    substr = s[i:i+t_l]
    match_count = 0
    for j in range(t_l):
        if substr[j] == t[j]:
            match_count += 1
    max_match_count = max(max_match_count, match_count)
print(t_l - max_match_count)
