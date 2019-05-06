S = list(input())
for i in range(len(S)):
    if(S[i]=="O"):
        S[i]="A"
    elif(S[i]=="A"):
        S[i]="O"
print("".join(S))

