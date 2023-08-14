sum_digit = sum(list(map(int, list(input()))))
print("Yes" if sum_digit % 9 == 0 else "No")
