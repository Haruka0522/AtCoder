S = list(input())
T = list(input())
list_at = ["a", "t", "c", "o", "d", "e", "r", "@"]
for i in range(len(S)):
    if (S[i] != T[i]):
        if (S[i] == "@" and not (T[i] in list_at)):
            print("You will lose")
            exit()
        elif (T[i] == "@" and not (S[i] in list_at)):
            print("You will lose")
            exit()
        elif (S[i] != "@" and T[i] != "@"):
            print("You will lose")
            exit()

print("You can win")
