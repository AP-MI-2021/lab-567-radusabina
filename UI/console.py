from Domain.cheltuiala import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala


def print_meniu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("a. Afisare cheltuieli")
    print("x. Iesire")

def ui_adauga_cheltuiala(lista):
    numar_apartament = input("Dati numarul apartamentului: ")
    suma = input("Dati suma: ")
    data = input("Dati data (DD.MM.YYYY): ")
    tipul = input("Dati tipul: ")
    return adauga_cheltuiala(numar_apartament, suma, data, tipul, lista)


def ui_sterge_cheltuiala(lista):
    numar_apartament = input("Dati numarul apartamentului de sters: ")
    return sterge_cheltuiala(numar_apartament, lista)

def show_all(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def run_menu(lista):
    while True:
        print_meniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_cheltuiala(lista)
        elif optiune == "2":
            lista = ui_sterge_cheltuiala(lista)
        elif optiune.lower() == "a":
            show_all(lista)
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune invalida ! Reincercati..")