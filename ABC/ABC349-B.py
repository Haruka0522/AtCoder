s = input()
s_set = set(list(s))
count = {i : [] for i in range(1, 101)}
for i in s_set:
    c = s.count(i)
    count[c].append(i)

for i in range(1, 101):
    if len(count[i]) != 2 and len(count[i]) != 0:
        print("No")
        exit()
print("Yes")
