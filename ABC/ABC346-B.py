s = "wbwbwwbwbwbw"*18
w,b = map(int,input().split())

for i in range(12*18-(w+b)):
    subs = s[i:i+w+b]
    if subs.count('w') == w and subs.count('b') == b:
        print("Yes")
        exit()
print("No")
