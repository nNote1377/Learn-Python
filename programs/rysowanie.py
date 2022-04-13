#importowanie bibloteki "turtle"
from turtle import *

#Wybór programu
print("1. Rysowanie kwadratu")
print("2. Rysowannie prostokątu")
print("3. Rysowanie trójkąta")
wybierz_program = int(input("Wybierz program wpisując liczbę od 1 do 3: "))

if wybierz_program == 1:
    #Rysowanie Kwadratu
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

elif wybierz_program == 2:
    #Rysowanie Prostokąta
    forward(150)
    right(90)
    forward(100)
    right(90)
    forward(150)
    right(90)
    forward(100)

elif wybierz_program == 3:
    #Rysowanie Trójkąta
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)


#Kreatywne zapętlenie programu
x=1
penup()
while True:
    forward(-x)
    forward(x)
    speed(x-1)

    x+=1