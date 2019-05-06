kouho_moji = list(input())
nanbanme = int(input())
a = nanbanme//5
b = nanbanme%5
if(b==0):
    a -= 1
print(kouho_moji[a],end="")
print(kouho_moji[b-1])
