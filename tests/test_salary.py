from faker_pk import FakerPK

def test_salary(faker_pk: FakerPK):
    s = faker_pk.salary()
    assert isinstance(s, int)
    assert s > 0
