from Domain.cheltuiala import creeaza_cheltuiala, get_numar_apartament, get_id


def adauga_cheltuiala(id, numar_apartament, suma, data, tipul, lista):
    """
    adauga o cheltuiala intr-o lista
    :param lista: lista de cheltuieli
    :param id: int
    :param numar_apartament: string
    :param suma: float
    :param data: string
    :param tipul: string
    :return: o lista continand atat elemente vechi, cat si noua cheltuiala
    """
    cheltuiala = creeaza_cheltuiala(id, numar_apartament, suma, data, tipul)
    return lista + [cheltuiala]


def get_by_id(id, lista):
    """
    Gaseste o cheltuiala cu numarul de apartament dat intr-o lista
    :param id: id-ul apartamentului
    :param lista: lista de cheltuieli
    :return: cheltuiala cu numarul de apartament dat din lista, sau None daca aceasta nu exista
    """
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def sterge_cheltuiala(id, lista):
    """
    Sterge un apartament cu numarul dat
    :param id: id-ul apartamentului care se va sterge
    :param lista: lista de cheltuieli
    :return: o lista de cheltuieli fara cheltuiala care are numarul apartamentului dat
    """
    rezultat = []
    for cheltuiala in lista:
        if get_id(cheltuiala) != id:
            rezultat.append(cheltuiala)
    return rezultat


def modifica_cheltuiala(id, numar_apartament, suma, data, tipul, lista):
    """
    Modifica o cheltuiala cu numarul apartamentului dat
    :param id: id-ul cheltuielii
    :param numar_apartament: numarul de apartament al cheltuielii
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tipul: tipul cheltuielii
    :param lista: lista cu cheltuieli
    :return: lista modificata
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            cheltuiala_noua = creeaza_cheltuiala(id, numar_apartament, suma, data, tipul)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
