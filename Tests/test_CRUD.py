from Domain.cheltuiala import get_numar_apartament, get_suma, get_data, get_tipul
from Logic.CRUD import adauga_cheltuiala, get_by_numar_apartament, sterge_cheltuiala, modifica_cheltuiala


def test_adauga_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(23, 230, "04.09.2021", "apa", lista)

    assert len(lista) == 1
    assert get_numar_apartament(get_by_numar_apartament(23, lista)) == 23
    assert get_suma(get_by_numar_apartament(23, lista)) == 230
    assert get_data(get_by_numar_apartament(23, lista)) == "04.09.2021"
    assert get_tipul(get_by_numar_apartament(23, lista)) == "apa"


def test_sterge_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(13, 150, "06.10.2021", "canal", lista)
    lista = adauga_cheltuiala(45, 200, "23.10.2021", "apa", lista)

    lista = sterge_cheltuiala(13, lista)

    assert len(lista) == 1
    assert get_by_numar_apartament(13, lista) is None
    assert get_by_numar_apartament(45, lista) is not None


def test_modifica_cheltuiala():
    lista = []
    lista = adauga_cheltuiala("1", 234, "12.02.2021", "canal", lista)
    lista = adauga_cheltuiala("23", 120, "23.10.2021", "apa", lista)

    lista = modifica_cheltuiala("23", 230, "04.10.2021", "curent", lista)

    assert len(lista) == 2
    cheltuiala_modificata = get_by_numar_apartament("23", lista)
    assert get_suma(cheltuiala_modificata) == 230
    assert get_data(cheltuiala_modificata) == "04.10.2021"
    assert get_tipul(cheltuiala_modificata) == "curent"
    cheltuiala_nemodificata = get_by_numar_apartament("1", lista)
    assert get_suma(cheltuiala_nemodificata) == 234
    assert get_data(cheltuiala_nemodificata) == "12.02.2021"
    assert get_tipul(cheltuiala_nemodificata) == "canal"
