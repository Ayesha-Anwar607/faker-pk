from faker_pk import FakerPK

def test_bank_name(faker_pk: FakerPK):
    b = faker_pk.bank_name()
    assert isinstance(b, str)
    assert len(b) > 0
