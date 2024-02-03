n = int(input())
a = list(map(int, input().split()))
saisyoujoutai = 0
kyakusu = 0
for i in range(n):
    kyakusu += a[i]
    if kyakusu < saisyoujoutai:
        saisyoujoutai = kyakusu
syokiti = abs(saisyoujoutai)
print(kyakusu + syokiti)
