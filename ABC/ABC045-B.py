A_cards = list(input())
B_cards = list(input())
C_cards = list(input())
who = "a"
while(True):
    if(who == "a"):
        if(len(A_cards)==0):
            print("A")
            exit()
        else:
            who = A_cards[0]
            del A_cards[0]
    elif(who == "b"):
        if(len(B_cards)==0):
            print("B")
            exit()
        else:
            who = B_cards[0]
            del B_cards[0]
    else:    
        if(len(C_cards)==0):
            print("C")
            exit()
        else:
            who = C_cards[0]
            del C_cards[0]

