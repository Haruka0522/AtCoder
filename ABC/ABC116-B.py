s = int(input())
checked = [s,]
for i in range(10**7):
    if checked[i] % 2 == 0:
        a_i = checked[i] // 2
    else:
        a_i = 3 * checked[i] + 1
    if a_i in checked:
        print(i+2)
        break
    checked.append(a_i)
#print(checked)

