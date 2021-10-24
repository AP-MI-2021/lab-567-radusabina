from Domain.cheltuiala import creeaza_cheltuiala, get_numar_apartament, get_suma, get_data, get_tipul


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala("2", 100, "12.03.2021", "canal")

    assert get_numar_apartament(cheltuiala) == "2"
    assert get_suma(cheltuiala) == 100
    assert get_data(cheltuiala) == "12.03.2021"
    assert get_tipul(cheltuiala) == "canal"
