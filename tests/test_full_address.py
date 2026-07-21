def test_full_address(faker_pk):
    addr = faker_pk.full_address()
    assert isinstance(addr, str)
    assert len(addr) > 0
    assert "," in addr
