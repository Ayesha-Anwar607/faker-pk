def test_city(faker_pk):
    c = faker_pk.city()
    assert isinstance(c, str)
    assert len(c) > 0
