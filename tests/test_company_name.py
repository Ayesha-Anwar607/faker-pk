from faker_pk import FakerPK

def test_company_name(faker_pk: FakerPK) -> None:
    c = faker_pk.company_name()
    assert isinstance(c, str)
    assert len(c) > 0
