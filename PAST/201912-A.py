def small_letters():
    return [chr(i) for i in range(97, 97+26)]
S = str(input())
try:
    print(int(S)*2)
except:
    print("error")
