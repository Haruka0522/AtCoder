x = int(input())

def is_prime(q):
    import math
    if q == 1:
        return False
    for k in range(2,int(math.sqrt(q)) + 1):
        if q % k == 0:
            return False
    return True

while True:
    if is_prime(x):
        print(x)
        exit()
    x += 1
