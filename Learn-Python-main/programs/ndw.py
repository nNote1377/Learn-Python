a=int(input("Wpisz: "))
b=int(input("Wpisz: "))
while a != b:
    if a > b:
        a = a - b
        print(a)
    else:
        b = b - a
        print(a)

print(a)