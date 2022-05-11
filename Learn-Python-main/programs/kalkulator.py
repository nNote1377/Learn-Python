#Otwieranie pętli która działa do momentu wyłaczenia programu
koniec=1
while koniec!=0:
    #Wybór działania
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgi")
    print("6. Pierwiastek")
    print("7. Wyłącz program")
    x=str(input('Jaki typ działania chcesz wykonać: '))
    if x=='1':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        c=float(a+b)
        print( a ,"+", b, "=", c)
    elif x=='2':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        c=float(a-b)
        print( a ,"-", b, "=", c)
    elif x=='3':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        c=float(a*b)
        print( a ,"*", b, "=", c)
    elif x=='4':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        if b==0:
            print('Ale ty głupi jesteś!!!')
        else:
            c=float(a/b)
            print( a ,"/", b, "=", c)
    elif x=='5':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        c=float(a**b)
        print( a ,"^", b, "=", c)
    elif x=='6':
        a=float(input('Wpisz 1. liczbe '))
        c=float(a**0.5)
        print("√", a, "=", c)
    elif x=='7':
        koniec-=1
    else:
        print('Ale ty głupi jesteś!!!')