user_choise =-1
cars = [ ]
drivers = []


def load_cars_file():
    try:

        file =open("cars.txt")
        for line in file.readlines():
            cars.append(line.strip())
        file.close()
    except FileNotFoundError:
        return

def load_drivers_file():
    try:
        file_a = open("drivers.txt")
        for line in file_a.readlines():
            drivers.append(line.strip())
        file_a.close()
    except FileNotFoundError :
        return


def show_cars():
    cars_index = 0
    for car in cars:
        print(car +" [ " + str(cars_index) +"]")
        cars_index +=1
def show_drivers():
    drivers_index = 0 
    for driver in drivers:
        print(driver + "[" + str(drivers_index) + "]")
        drivers_index +=1
def add_driver():
    driver = input("Podaj Imie i Nazwisko Kierowcy  :")
    drivers.append(driver)
    print("Dodano Kierowce")
def delete_driver():
     show_drivers()
     driver_index = int(input("Podaj którego kierowce chce usunac :   "))
     if driver_index <0 or driver_index >len(drivers) -1:
         print("Kierowca o tym numerze nie istnieje ")
         return 
     drivers.pop(driver_index)
     print("Usunieto Kierowce")
def add_car():
    car = input("Podaj marke samochodu")
    cars.append(car)
    print("Dodano Samochód")

def delete_car():
    show_cars()
    car_index = int(input("Podaj który samochód chcesz usunac :"))
    if car_index <0 or car_index > len(cars)-1:
        print("W bazie nie ma takiego samochodu")
        return
    cars.pop(car_index)
    print("Usunieto samochód")

def car_to_file():
    file = open("cars.txt" , "w")
    for car in cars:
        file.write(car + "\n")
    file.close
def drivers_to_file():
    file_a = open("drivers.txt" , "w")
    for driver in drivers:
        file_a.write(driver +"\n")

    file_a.close



load_cars_file()
load_drivers_file()


while user_choise !=8:
    if(user_choise ==1):
        # print("Wyswietłamy liste samochodów")
        show_cars()
    if(user_choise ==2):
        show_drivers()   
    if(user_choise ==3):
        # print("dodamy kierowce")
        add_driver()
    if(user_choise ==4):
        delete_driver()
    if(user_choise ==5):
        add_car()

    if(user_choise == 6):
        delete_car()
    if(user_choise ==7):
        car_to_file()
        drivers_to_file()
    

    
    
    
    
    print()
    print("1 : Wysiwietl Liste Pojazdów")
    print("2 : Wyswietl Liste Kierowcow ")
    print("3 : Dodaj Kierowce")
    print("4 : Usun kierowce ")
    print("5: Dodaj Pojazd")
    print("6 : Usuń Pojazd")
    print("7: Zapisz zmiany do plików")
    print("8: Wyjdz")
    user_choise = int(input("Wybierz co chcesz zrobic : "))
    print()
