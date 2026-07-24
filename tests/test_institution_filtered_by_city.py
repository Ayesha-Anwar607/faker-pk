from faker_pk import FakerPK
from faker_pk.utils import query_value

def test_institution_filtered_by_city(faker_pk: FakerPK):
    inst = faker_pk.institution(city="Lahore")
    assert isinstance(inst, str)
    inst_city = query_value("SELECT city FROM institutions WHERE name = ?", (inst,))
    assert inst_city == "Lahore"
