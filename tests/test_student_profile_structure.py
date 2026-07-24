from faker_pk import FakerPK

def test_student_profile_structure(faker_pk: FakerPK):
    profile = faker_pk.student_profile()
    assert isinstance(profile, dict)
    required_keys = ["name", "gender", "cnic", "institution", "level", "city", "province", "dob"]
    for key in required_keys:
        assert key in profile
        assert profile[key] is not None
