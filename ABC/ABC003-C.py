Takahashi_rate = 0
N,K = map(int,input().split())
Rates = list(map(int,input().split()))
Rates.sort(reverse=True)
miru_douga = Rates[:K]
miru_douga.sort(reverse=False)
for i in miru_douga:
    Takahashi_rate = (Takahashi_rate+i)/2
print(Takahashi_rate)