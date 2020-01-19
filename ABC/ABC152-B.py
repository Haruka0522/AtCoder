a,b = map(int,input().split())
A = str(a)*b
B = str(b)*a
print(sorted([A,B])[0])
