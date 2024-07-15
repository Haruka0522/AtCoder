n, x = map(int, input().split())
s = input()
new_op = []

for op in s:
    if op == "U" and len(new_op) > 0 and (new_op[-1] == "L"  or new_op[-1] == "R"):
        new_op.pop()
    else:
        new_op.append(op)

for op in new_op:
    if op == "U":
        x = x//2
    elif op == "L":
        x = 2*x
    elif op == "R":
        x = 2*x+1

print(x)
