from faker_pk import FakerPK

def test_industry_name(faker_pk: FakerPK):
    i = faker_pk.industry_name()
    assert isinstance(i, str)
    assert len(i) > 0
