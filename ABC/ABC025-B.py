N,A,B = map(int,input().split())
zahyo = 0
for i in range(N):
    s,d = input().split()
    d = int(d)
    if(s == "East"):
        if(d < A):
            zahyo += A
        elif(d > B):
            zahyo += B
        else:
            zahyo += d
    else:
        if(d < A):
            zahyo -= A
        elif(d > B):
            zahyo -= B
        else:
            zahyo -= d
if(zahyo < 0):
    print("West "+str(abs(zahyo)))
elif(zahyo > 0):
    print("East "+str(zahyo))
else:
    print(0)
