x = int(input())

#コピペ
def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1
#コピペ終わり

while(True):
    if is_prime(x):
        print(x)
        exit()
    x += 1
