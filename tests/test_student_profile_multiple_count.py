from faker_pk import FakerPK

def test_student_profile_multiple_count(faker_pk: FakerPK):
    profiles = faker_pk.student_profile(count=5)
    assert isinstance(profiles, list)
    assert len(profiles) == 5
    for p in profiles:
        assert isinstance(p, dict)
        assert "institution" in p