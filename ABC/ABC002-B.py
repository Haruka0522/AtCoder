remove_list = ["a","i","u","e","o"]
W = list(input())
for i in remove_list:
    while(1):
        try:
            W.remove(i)
        except:
            break

print("".join(W))