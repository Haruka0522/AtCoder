S = list(input())
flag = 0
for i in range(2):
    if (len(S) == 0):
        print("YES")
        exit()

    if (flag == 0):
        if (S[-2::] == ["c", "h"]):
            del S[-2::]
            flag = 1
        else:
            flag = 2

        if (S[-1] in ["o", "k", "u"]):
            del S[-1]
            flag = 1
        else:
            flag = 2

    elif (flag == 1):
        if (S[-2::] == ["c", "h"]):
            print("YES")
        else:
            flag = 2

        if (S[-1] in ["o", "k", "u"]):
            print("YES")
        else:
            flag = 2

        if (len(S) == 0):
            print("YES")
        else:
            flag = 2

if (flag == 2):
    print("NO")
