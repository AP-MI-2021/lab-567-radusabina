from Tests.test_CRUD import test_adauga_cheltuiala, test_sterge_cheltuiala, test_modifica_cheltuiala
from Tests.test_domain import test_cheltuiala


def test_all():
    test_cheltuiala()
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
    test_modifica_cheltuiala()

