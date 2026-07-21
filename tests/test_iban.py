from faker_pk import FakerPK

def test_iban(faker_pk: FakerPK):
    i = faker_pk.iban()
    assert isinstance(i, str)
    assert i.startswith("PK")
