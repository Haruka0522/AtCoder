m = int(input())
if(m<100):
    print("00")
elif(m<=5000):
    if(m/100 < 10):
        print(str(0)+str(m//100))
    else:
        print(int(m/100))
elif(m<=30000):
    print(int(m/1000+50))
elif(m<=70000):
    print(int((m/1000 - 30)/5 +80))
else:
    print(89)