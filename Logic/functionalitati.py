from Domain.cheltuiala import get_numar_apartament, get_data, get_suma, creeaza_cheltuiala, get_id, get_tipul


def sterge_toate_cheltuielile_apartament(numar_aparatament, lista):
    """
    Ștergerea tuturor cheltuielilor pentru un apartament dat.
    :param numar_aparatament: numarul de apartament pentru care dorim sa stergem toate cheltuielile
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cele pentru numarul de apartament specificat
    """
    rezultat = []
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) != numar_aparatament:
            rezultat.append(cheltuiala)
    return rezultat


def adauga_valoare_data(data, valoare, lista):
    """
    Adunarea unei valori la toate cheltuielile dintr-o dată citită.
    :param valoare: valoarea care se adauga sumei
    :param data: data pentru care se va adauga o valoare
    :param lista: lista de cheltuieli
    :return: lista in care cheltuielile cu data introdusa au valoarea adaugata sumei
    """
    if valoare < 0:
        raise ValueError("Nu se poate adauga o valoare negativa !")
    rezultat = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            cheltuiala_noua = creeaza_cheltuiala(get_id(cheltuiala), get_numar_apartament(cheltuiala),
                                                 float(get_suma(cheltuiala)) + valoare, get_data(cheltuiala),
                                                 get_tipul(cheltuiala))
            rezultat.append(cheltuiala_noua)
        else:
            rezultat.append(cheltuiala)
    return rezultat


def cea_mai_mare_cheltuiala_dupa_tip(lista):
    """
    Determina cea mai mare cheltuiala pentru fiecare tip de cheltuială
    :param lista: lista de chetuieli
    :return: cea mai mare chetuiala pentru fiecare tip de cheltuiala
    """
    rezultat = {}
    for cheltuiala in lista:
        tipul = get_tipul(cheltuiala)
        suma = get_suma(cheltuiala)
        if tipul in rezultat:
            if suma > get_suma(rezultat[tipul]):
                rezultat[tipul] = cheltuiala
        else:
            rezultat[tipul] = cheltuiala
    return rezultat


def ordonare_descrescator_cheltuieli_dupa_suma(lista):
    """
    Ordoneaza cheltuielile descrescător după sumă.
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli ordoonata descrescator dupa suma
    """
    return sorted(lista, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)
