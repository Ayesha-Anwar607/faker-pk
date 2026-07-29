from faker_pk import FakerPK

def test_student_profile_gender_cnic_alignment(faker_pk: FakerPK):
    for _ in range(20):
        profile = faker_pk.student_profile()
        gender = profile["gender"]
        last_digit = int(profile["cnic"][-1])
        if gender == "male":
            assert last_digit % 2 == 1, f"Male CNIC should end with an odd digit, got {profile['cnic']}"
        else:
            assert last_digit % 2 == 0, f"Female CNIC should end with an even digit, got {profile['cnic']}"