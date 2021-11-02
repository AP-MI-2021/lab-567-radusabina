from Tests.test_CRUD import test_adauga_cheltuiala, test_sterge_cheltuiala, test_modifica_cheltuiala, test_get_by_id, \
    test_get_by_numar_apartament
from Tests.test_domain import test_cheltuiala
from Tests.test_functionalitati import test_sterge_toate_cheltuielile_apartament, test_adauga_valoare_data, \
    test_cea_mai_mare_cheltuiala_dupa_tip, test_ordonare_descrescator_cheltuieli


def test_all():
    test_cheltuiala()
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
    test_modifica_cheltuiala()
    test_get_by_id()
    test_get_by_numar_apartament()
    test_sterge_toate_cheltuielile_apartament()
    test_adauga_valoare_data()
    test_cea_mai_mare_cheltuiala_dupa_tip()
    test_ordonare_descrescator_cheltuieli()
