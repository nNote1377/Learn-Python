#W tym programie obliczysz swój wiek

#Pytanie o roku urodzenie używając polecenia input
rok_urodzenia = int(input("Podaj rok urodzenia: "))

#Pytanie o aktualny rok
aktualny_rok = int(input("Podaj aktualny rok: "))

#Obliczanie wieku
wiek = aktualny_rok - rok_urodzenia

#Wydrukowanie wieku w konsoli
print("Masz", wiek, "lat")