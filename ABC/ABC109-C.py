'''自力WA（python3.4.3)
import fractions
N,X = map(int,input().split())
x_list = list(map(int,input().split()))
sa = []
x_list.sort()import fractions
N,X = map(int,input().split())
x_list = list(map(int,input().split()))
sa = []
x_list.sort()
for i in range(N-1):
    sa.append(x_list[i+1]-x_list[i-1])
gcd = 0
for i in range(len(sa)-1):
    gcd = max(gcd,fractions.gcd(sa[i],sa[i+1]))
print(gcd)import fractions
N,X = map(int,input().split())
x_list = list(map(int,input().split()))
sa = []
x_list.sort()
for i in range(N-1):
    sa.append(x_list[i+1]-x_list[i])
gcd = 0
for i in range(len(sa)-1):
    gcd = max(gcd,fractions.gcd(sa[i],sa[i+1]))
if N == 1:
    print(x_list[0]-N)
else:
    print(gcd)
for i in range(N-1):
    sa.append(x_list[i+1]-x_list[i-1])
print(fractions.gcd(sa))
'''

