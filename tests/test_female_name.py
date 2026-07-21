def test_female_name(faker_pk):
    name = faker_pk.female_name()
    assert isinstance(name, str)
    assert len(name) > 0
