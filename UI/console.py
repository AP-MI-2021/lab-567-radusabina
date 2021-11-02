from Domain.cheltuiala import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.functionalitati import sterge_toate_cheltuielile_apartament, adauga_valoare_data, \
    cea_mai_mare_cheltuiala_dupa_tip, ordonare_descrescator_cheltuieli


def print_meniu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Sterge toate cheltuielile pentru un apartament dat")
    print("5. Aduna o valoare la toate cheltuielile dintr-o dată citită")
    print("6. Determina cea mai mare cheltuiala pentru fiecare tip de cheltuială")
    print("7. Ordoneaza cheltuielile descrescător după sumă.")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def ui_adauga_cheltuiala(lista):
    try:
        id = int(input("Dati id-ul cheltuielii: "))
        numar_apartament = input("Dati numarul apartamentului: ")
        suma = input("Dati suma: ")
        data = input("Dati data (DD.MM.YYYY): ")
        tipul = input("Dati tipul: ")
        return adauga_cheltuiala(id, numar_apartament, suma, data, tipul, lista)
    except ValueError as ve:
        print(f"Eroare : {ve}")
        return lista


def ui_sterge_cheltuiala(lista):
    try:
        id_de_sters = int(input("Dati id-ul cheltuielii de sters: "))
        lista = sterge_cheltuiala(id_de_sters, lista)
        return lista
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_modifica_cheltuiala(lista):
    try:
        id = int(input("Dati id-ul cheltuielii de modificat: "))
        numar_apartament = input("Dati noul numar de apartament: ")
        suma = float(input("Dati noua suma: "))
        data = input("Dati noua data (DD.MM.YYYY): ")
        tipul = input("Dati noul tip: ")
        return modifica_cheltuiala(id, numar_apartament, suma, data, tipul, lista)
    except ValueError as ve:
        print(f"Eroare : {ve}")
        return lista


def show_all(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def ui_sterge_toate_cheltuielile_apartament(lista):
    try:
        numar_apartament = input("Dati numarul apartamentului pentr care doriti sa stergeti toate cheltuielile: ")
        print("Stergerea a fost efectuata cu succes !")
        return sterge_toate_cheltuielile_apartament(numar_apartament, lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_adauga_valoare_data(lista):
    try:
        data = input("Introduceti data la care doriti sa adaugati valoarea: ")
        valoare = float(input("Introduceti valoarea pe care doriti sa o adaugati: "))
        return adauga_valoare_data(data, valoare, lista)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return lista


def ui_cea_mai_mare_cheltuiala_dupa_tip(lista):
    if not lista:
        print("Nu exista cheltuieli in lista !")
        return lista
    rezultat = cea_mai_mare_cheltuiala_dupa_tip(lista)
    for tip in rezultat:
        print(f"Cheltuiala {tip} are valoarea maxima de {rezultat[tip]} lei")


def ui_ordonare_descrescator_cheltuieli(lista):
    if not lista:
        print("Nu exista cheltuieli in lista !")
        return lista
    else:
        return show_all(ordonare_descrescator_cheltuieli(lista))


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
        elif optiune == "4":
            lista = ui_sterge_toate_cheltuielile_apartament(lista)
        elif optiune == "5":
            lista = ui_adauga_valoare_data(lista)
        elif optiune == "6":
            ui_cea_mai_mare_cheltuiala_dupa_tip(lista)
        elif optiune == "7":
            ui_ordonare_descrescator_cheltuieli(lista)
        elif optiune.lower() == "a":
            show_all(lista)
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune invalida ! Reincercati..")
