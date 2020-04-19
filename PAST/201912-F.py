S = input()
N = len(S)
def small_letters():
    return [chr(i) for i in range(97, 97+26)]
def capital_letters():
    return [chr(i) for i in range(65, 65+26)]
SL = small_letters()
CL = capital_letters()
split_list = []
for i in range(N):
    if S[i] in CL:
        split_list.append(i)
ans = []
for i in range(0,len(split_list),2):
    start = split_list[i]
    end = split_list[i+1]
    ans.append(S[start:end+1])
ans.sort(key=str.lower)
print("".join(ans))
