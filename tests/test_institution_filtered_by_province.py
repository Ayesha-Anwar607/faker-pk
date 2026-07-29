from faker_pk import FakerPK
from faker_pk.utils import query_value

def test_institution_filtered_by_province(faker_pk: FakerPK):
    inst = faker_pk.institution(province="Khyber Pakhtunkhwa")
    assert isinstance(inst, str)
    inst_province = query_value(
        "SELECT l.province FROM institutions i JOIN locations l ON i.city = l.city WHERE i.name = ?",
        (inst,)
    )
    assert inst_province == "Khyber Pakhtunkhwa"
