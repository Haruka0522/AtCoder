n = input()
def small_letters():
    return [chr(i) for i in range(97, 97+26)]
def capital_letters():
    return [chr(i) for i in range(65, 65+26)]
if n in small_letters():
    print("a")
else:
    print("A")
