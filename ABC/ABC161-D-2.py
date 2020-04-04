f = open("test.txt")
line = f.readline()
result = []
i = 1
while line:
    if i >= 10 and i % 10 == 0:
        result.append(int(line))
    line = f.readline()
    i += 1
f.close
print(result)
