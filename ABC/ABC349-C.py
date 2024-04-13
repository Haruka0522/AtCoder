s = input()
t = input()

s = s.upper()

if t[2] == "X":
    g = 2
else:
    g = 3

t_i = 0
for i in range(len(s)):
    if s[i] == t[t_i]:
        t_i += 1
        if t_i == g:
            print("Yes")
            exit()
print("No")
