S = list(input())
for num,letter in enumerate(S):
    num += 1 
    if num % 2 == 1:
        if letter != "R" and letter != "U" and letter != "D":
            print("No")
            exit()
    else:
        if letter != "L" and letter != "U" and letter != "D":
            print("No")
            exit()
print("Yes")
