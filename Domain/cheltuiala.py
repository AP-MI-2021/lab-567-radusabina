def creeaza_cheltuiala(numar_apartament, suma, data, tipul):
    """
    Creeaza un dictionar ce reprezinta o cheltuiala
    :param numar_apartament: string
    :param suma: float
    :param data: string
    :param tipul: string
    :return:
    """
    return {
        "numar_apartament": numar_apartament,
        "suma": suma,
        "data": data,
        "tipul": tipul

    }

def get_numar_apartament(cheltuiala):
    """
    Returneaza numarul apartamentului unei cheltuieli
    :param cheltuiala: dictionatul ce contine o cheltuiala
    :return: numarul apartamentului cheltuielii
    """
    return cheltuiala["numar_apartament"]


def get_suma(cheltuiala):
    """
    Returneaza suma cheltuielii
    :param cheltuiala: dictionarul ce contine o cheltuiala
    :return: suma cheltuielii
    """
    return cheltuiala["suma"]


def get_data(cheltuiala):
    """
    Returneaza data cheltuielii
    :param cheltuiala: dictionarul ce contine o cheltuiala
    :return: data cheltuielii
    """
    return cheltuiala["data"]


def get_tipul(cheltuiala):
    """
    Returneaza tipul cheltuielii
    :param cheltuiala: dictionarul ce contine o cheltuiala
    :return: tipul cheltuielii
    """
    return cheltuiala["tipul"]


def to_string(cheltuiala):
    """
    Returneaza cheltuiala ca string
    :param cheltuiala: dictionarul ce contine o cheltuiala
    :return: cheltuiala ca string
    """
    return "Numar apartament: {}; Suma: {}; Data: {}; Tipul: {}".format(
        get_numar_apartament(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tipul(cheltuiala)
    )