N = int(input())
S = list(input())
jisyo = {"1":0,"2":0,"3":0,"4":0}
for i in S:
    jisyo[i] += 1
print(max(jisyo.values()),min(jisyo.values()))

