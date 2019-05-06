import datetime
seconds = int(input())

henkango = datetime.timedelta(seconds=seconds)
if(len(list(str(henkango).split(":")[0]))==1):
    print(0,end="")
print(henkango)