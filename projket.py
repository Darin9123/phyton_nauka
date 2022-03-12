import random

nagrody_ze_skrzynki = ["zielona" , "pomaranczowa" , "legendarna" , "ultralegendarna"]
moja_biblioteka_skorek = []
print ("Witaj w mojej grze ")

token = 100
szynka_podst = 10
szkrzynka_srednia = 20
skrzynka_legendarna = 50
skrzynka_ultra = 80
user_choice = -1

def show_tokens(token) :
    print( "Posiadasz obecnie ", token  , "Monet ")
def add_tokens(token):
    dodane_tokeny = int(input("Podaj liczbe która chcesz dodac "))
    token = token + dodane_tokeny
    print(token)
def podstawowa():
    pozoztały_token = token - szynka_podst
    print("Posiadasz jescze " , pozoztały_token ,  "Monet")
    skorka = random.choices(nagrody_ze_skrzynki, [90,9,1,0] , k = 1)
    moja_biblioteka_skorek.append(skorka)
    print("Zdobyta skórka to " ,skorka )
    print("Posiadasz obecnie nastepujace skorki" , moja_biblioteka_skorek)

def srednia():
    pozostały_token = token - szkrzynka_srednia
    print ( "Posiadasz jescze " , pozostały_token ,  "Monet")
    skorka = random.choices(nagrody_ze_skrzynki , [0.65,0.3,0.048,0.002], k= 1)
    moja_biblioteka_skorek.append(skorka)
    print("Zdobyta skorka to " , skorka)
def legenda():
    pozostały_token = token - skrzynka_legendarna
    print ( "Posiadasz jescze " , pozostały_token ,  "Monet")
    skorka = random.choices(nagrody_ze_skrzynki , [0.0 , 0.90, 0.9, 0.1] , k =1)
    moja_biblioteka_skorek.append(skorka)
    print("Zdobyłes skorke " , skorka)
def ultra() :
    pozostały_token = token - skrzynka_ultra
    print("Posiadasz jescze" , pozostały_token , "Monet") 
    skorka  = random.choices(nagrody_ze_skrzynki , [0.0 , 0.40,0.45, 0.15] , k =1)
    moja_biblioteka_skorek.append(skorka)
    print("Zdobyłes skorke " , skorka)  

def show_my_skins() :
    print(moja_biblioteka_skorek)


while  user_choice != 8 :
    if user_choice == 1:
        show_tokens(token)
    if user_choice == 2:
        add_tokens(token)    
    if user_choice == 3 :
        podstawowa()
    if user_choice == 4 :
        srednia()
    if user_choice == 5 :
        legenda()
    if(user_choice == 6):
        ultra()
    if(user_choice == 7):
        show_my_skins()    

    
    
    print()
    print("1. Pokaż ile mam monet ")
    print("2. Dodaj monety ")
    print("3. Otwórz skrzyke podst ")
    print("4. Otworz srednia skrzynke")
    print("5. Otwórz legendarna skrzynke ")
    print("6. Otwórz skrzynke ultra ")
    print("7. Wyswietl Moje Skorki")
    print("8.Wyjdz")
    user_choice = int(input("Wybierz liczbe :"))
    print()
