from faker_pk import FakerPK
from faker_pk.utils import query_row

def test_student_profile_consistency(faker_pk: FakerPK):
    for _ in range(20):
        profile = faker_pk.student_profile(province="Punjab")
        assert profile["province"] == "Punjab"
        row = query_row(
            "SELECT i.city, l.province FROM institutions i JOIN locations l ON i.city = l.city WHERE i.name = ?",
            (profile["institution"],)
        )
        assert row is not None
        assert row[0] == profile["city"]
        assert row[1] == profile["province"]
