n = [int(i) for i in input()]
sukimanokazu = len(n) - 1
for i in range(2 ** sukimanokazu):
    op = ["-"] * sukimanokazu #予め作っておくリスト
    for j in range(sukimanokazu):
        if (i >> j) & 1:
            op[sukimanokazu - 1 - j] = "+"  #フラグの場所を＋で上書き

    m = [str(k) for k in n]
    siki = m[0] + op[0] + m[1] + op[1] + m[2] + op[2] + m[3]
    if eval(siki) == 7:
        print(siki+"=7")
        exit()
