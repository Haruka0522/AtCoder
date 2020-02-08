from math import floor
def f(n):
    return floor((n**2+4)/8)
print(f(f(f(20))))
