import collections

s = list(input())

c = collections.Counter(s)

keys = c.keys()
for k in keys:
    if c[k] == 1:
        hen = k

for i in range(len(s)):
    if s[i] == hen:
        print(i+1)
