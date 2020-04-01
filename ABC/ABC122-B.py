S = input()
ans = 0
ACGT = ["A","C","G","T"]
for i in range(len(S)):
    for j in range(i,len(S)+1):
        clipped_list = list(S[i:j])
        clipped = set(clipped_list)
        for acgt in ACGT:
            try:
                clipped.remove(acgt)
            except:
                pass
        if clipped == set():
            ans = max(ans,len(clipped_list))

print(ans)

