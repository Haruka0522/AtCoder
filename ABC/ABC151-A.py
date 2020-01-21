C = input()

#アルファベットの小文字のリストを生成
def SmallLetters():
    return [chr(i) for i in range(97,97+26)]

SL = SmallLetters()

print(SL[SL.index(C)+1])
