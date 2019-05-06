train_tujo = int(input())
train_noriho = int(input())
bus_tujo = int(input())
bus_noriho = int(input())
train_yasui = 0
bus_yasui = 0

if(train_noriho > train_tujo):
    train_yasui = train_tujo
else:
    train_yasui = train_noriho

if(bus_noriho > bus_tujo):
    bus_yasui = bus_tujo
else:
    bus_yasui = bus_noriho

print(bus_yasui + train_yasui)
