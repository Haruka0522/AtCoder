h, w, n = map(int, input().split())
grid = [[".", ]*w for _ in range(h)]
x, y = 0, 0
d = "n"
def tokeimawari(d):
    if d == "n":
        return "e"
    if d == "e":
        return "s"
    if d == "s":
        return "w"
    if d == "w":
        return "n"
def hantokeimawari(d):
    if d == "n":
        return "w"
    if d == "w":
        return "s"
    if d == "s":
        return "e"
    if d == "e":
        return "n"
def susumu(x, y, d):
    if d == "n":
        if y - 1 < 0:
            return x, h-1
        else:
            return x, y-1
    if d == "e":
        if x + 1 >= w:
            return 0, y
        else:
            return x+1, y
    if d == "s":
        if y + 1 >= h:
            return x, 0
        else:
            return x, y+1
    if d == "w":
        if x - 1 < 0:
            return w-1, y
        else:
            return x-1, y

for i in range(n):
    if grid[y][x] == ".":
        grid[y][x] = "#"
        d = tokeimawari(d)
    else:
        grid[y][x] = "."
        d = hantokeimawari(d)
    x, y = susumu(x, y, d)
for i in range(h):
    print("" .join(grid[i]))

