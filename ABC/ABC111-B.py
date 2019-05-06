'''N = int(input())
if(N<=111):
    print("111")
elif(N<=222):
    print("222")
elif(N<=333):
    print("333")
elif(N<=444):
    print("444")
elif(N<=555):
    print("555")
elif(N<=666):
    print("666")
elif(N<=777):
    print("777")
elif(N<=888):
    print("888")
else:
    print("999")
'''

N = int(input())
a = N//111
if(N%111==0):
    print(N)
else:
    print((a+1)*111)