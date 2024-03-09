n = int(input())
s = input()
q = int(input())
abc_list = [chr(i) for i in range(97,97+26)]
converter = {abc_list[i]: abc_list[i] for i in range(26)}
for i in range(q):
    c, d = input().split()
    for j in abc_list:
        if converter[j] == c:
            converter[j] = d
            c_ok = True
for i in range(n):
    c = s[i]
    conv = converter[c]
    print(conv, end="")
