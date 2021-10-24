from Domain.cheltuiala import creeaza_cheltuiala, get_numar_apartament


def adauga_cheltuiala(numar_apartament, suma, data, tipul, lista):
    """
    adauga o cheltuiala intr-o lista
    :param numar_apartament: string
    :param suma: float
    :param data: string
    :param tipul: string
    :return: o lista continand atat elemente vechi, cat si noua cheltuiala
    """
    cheltuiala = creeaza_cheltuiala(numar_apartament, suma, data, tipul)
    return lista + [cheltuiala]


def get_by_numar_apartament(numar_apartament, lista):
    """
    Gaseste o cheltuiala cu numarul de apartament dat intr-o lista
    :param numar_apartament: numarul apartamentului
    :param lista: lista de cheltuieli
    :return: cheltuiala cu numarul de apartament dat din lista, sau None daca aceasta nu exista
    """
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            return cheltuiala
    return None


def sterge_cheltuiala(numar_apartament, lista):
    """
    Sterge un apartament cu numarul dat
    :param numar_apartament: numarul apartamentului care se va sterge
    :param lista: lista de cheltuieli
    :return: o lista de cheltuieli fara cheltuiala care are numarul apartamentului dat
    """
    return [cheltuiala for cheltuiala in lista if get_numar_apartament(cheltuiala) != numar_apartament]


def modifica_cheltuiala(numar_apartament, suma, data, tipul, lista):
    """
    Modifica o cheltuiala cu numarul apartamentului dat
    :param numar_apartament: numarul de apartament al cheltuielii
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tipul: tipul cheltuielii
    :param lista: lista cu cheltuieli
    :return: lista modificata
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            cheltuiala_noua = creeaza_cheltuiala(numar_apartament, suma, data, tipul)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
