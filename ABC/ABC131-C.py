#2WAがどうしても消せませんでした(泣)

#最大公約数
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
#最小公倍数
def lcm(x,y):
    return (x*y//gcd(x,y))
 
 
A,B,C,D = map(int,input().split())
CDlcm = lcm(C,D)
 
if C==D:
    print(B+1-A-(B//C-A//C)-1)
elif A==C or A==D or B==C or B==D:
    print(B+1-A-(B//C-A//C)-2)
else:
    c = (B+1)//C-A//C
    d = (B+1)//D-A//D
    e = (B+1)//CDlcm-A//CDlcm
    print((B-A+1)-c-d+e)
