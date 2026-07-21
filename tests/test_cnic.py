def test_cnic(faker_pk):
    c = faker_pk.cnic()
    assert isinstance(c, str)
    assert len(c) == 15   # 13 digits + 2 hyphens
    assert c[5] == "-"
    assert c[13] == "-"
