from Domain.cheltuiala import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala


def print_meniu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("a. Afisare cheltuieli")
    print("x. Iesire")

def ui_adauga_cheltuiala(lista):
    id = int(input("Dati id-ul cheltuielii: "))
    numar_apartament = input("Dati numarul apartamentului: ")
    suma = input("Dati suma: ")
    data = input("Dati data (DD.MM.YYYY): ")
    tipul = input("Dati tipul: ")
    return adauga_cheltuiala(id, numar_apartament, suma, data, tipul, lista)


def ui_sterge_cheltuiala(lista):
    id_de_sters = int(input("Dati id-ul cheltuielii de sters: "))
    lista = sterge_cheltuiala(id_de_sters, lista)
    print("Stergerea a fost efectuata cu succes")
    return lista



def ui_modifica_cheltuiala(lista):
    id = int(input("Dati id-ul cheltuielii de modificat: "))
    numar_apartament = input("Dati noul numar de apartament: ")
    suma = float(input("Dati noua suma: "))
    data = input("Dati noua data (DD.MM.YYYY): ")
    tipul = input("Dati noul tip: ")
    return modifica_cheltuiala(id, numar_apartament, suma, data, tipul, lista)


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
        elif optiune == "3":
            lista = ui_modifica_cheltuiala(lista)
        elif optiune.lower() == "a":
            show_all(lista)
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune invalida ! Reincercati..")