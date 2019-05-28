#最大公約数
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a


#最小公倍数
def lcm(x,y):
    return (x*y//gcd(x,y))


#アルファベットの小文字のリストを生成
def SmallLetters():
    return [chr(i) for i in range(97,97+26)]


#アルファベットの大文字のリストを生成
def CapitalLetters():
    return [chr(i) for i in range(65,65+26)]



