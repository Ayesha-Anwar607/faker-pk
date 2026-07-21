def test_male_name(faker_pk):
    name = faker_pk.male_name()
    assert isinstance(name, str)
    assert len(name) > 0
