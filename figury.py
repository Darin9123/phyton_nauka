import math
wybor = -1

def kwadrat(a):
    pole = a * a
    print ( "Pole kwadratu wynosi " , pole)

def pole_prostakata(a  , b):
    pole = a * b 
    print("Pole prostakata wynosi" , pole)

def pole_troj(a , h) :
    pole =  0.5 * a * h
    print ("Pole trojkata wynosi " , pole)

def pole_trapez(a , b, h) :
    pole = (a+b)/2 * h
    print("Pole trapezu wynosi" , pole)

def pole_kola(r):
    pole = math.pi * r**2
    print("Pole koła wynosi " , pole)

while(wybor != 6):
    if wybor == 1:
        bok = int(input("Podaj bok :"))
        kwadrat(bok)
    elif wybor ==2:
        bok1 = int(input("Podaj Pierwszy bok "))
        bok2 = int(input("Podaj drugi bok "))
        pole_prostakata(bok1, bok2)
    elif wybor ==3 :
        bok = int(input("Podaj Bok trójkata "))
        wys = int(input("Podaj wysokosc trojkata "))
        pole_troj(bok , wys)
    elif wybor == 4:
         bok1 = int(input("Podaj Pierwszy bok "))
         bok2 = int(input("Podaj drugi bok "))
         wys = int(input("Podaj wysokosc "))
         pole_trapez(bok1 , bok2, wys)
    elif wybor == 5 :
         promien = int(input("Podaj promien  ")) 
         pole_kola(promien)  





    print()
    print("1. Policz pole kwadratu")
    print("2.Policz pole prostokata")
    print("3. Policz pole trójkata ")
    print("4. Policz pole trapezu")
    print("5. Policz pole kola")
    print("6. Wyjdz z programu ")

    wybor = int(input("Wybierz co chesz zrobic  :"))
    print()

     