S = [input() for i in range(int(input()))]
ans = 0
first_B = 0
end_A = 0
for i in S:
    ans += i.count("AB")
    if(i[0] == "B"):
        first_B += 1
    if(i[-1] == "A"):
        end_A += 1
print(ans+min(first_B,end_A))
