alice,bob = map(int,input().split())
if(bob == 1 or alice == 1):
    if(bob == 1 and alice == 1):
        print("Draw")
    elif(bob == 1):
        print("Bob")
    else:
        print("Alice")
else:
    if(bob < alice):
        print("Alice")
    elif(alice < bob):
        print("Bob")
    else:
        print("Draw")