N= int(input())
a_li = list(map(int,input().split()))
a_conv = []
for i in a_li:
    if 1 <= i <= 399:
        a_conv.append(1)
    elif 400 <= i <= 799:
        a_conv.append(2)
    elif 800 <= i <= 1199:
        a_conv.append(3)
    elif 1200 <= i <= 1599:
        a_conv.append(4)
    elif 1600 <= i <= 1999:
        a_conv.append(5)
    elif 2000 <= i <= 2399:
        a_conv.append(6)
    elif 2400 <= i <= 2799:
        a_conv.append(7)
    elif 2800 <= i <= 3199:
        a_conv.append(8)
    elif 3200 <= i:
        a_conv.append(9)
free = a_conv.count(9)
ans_min = 0
ans_max = 0
if free == len(a_conv):
    ans_min = 1
    ans_max = free
else:
    for i in range(1,9):
        if i in a_conv:
            ans_min += 1
    ans_max = ans_min + free
print(ans_min,ans_max)
