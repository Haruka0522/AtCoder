N = int(input())
S = input()
alpha = [chr(i) for i in range(65,65+26)]
text = []
ans = []
for i in list(S):
    text.append(alpha.index(i))
for i in range(len(S)):
    text[i] = (text[i] + N) % 26
for i in range(len(S)):
    ans.append(alpha[text[i]])
print("".join(map(str,ans)))
