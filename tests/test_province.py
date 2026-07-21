def test_province(faker_pk):
    p = faker_pk.province()
    assert isinstance(p, str)
    assert len(p) > 0
