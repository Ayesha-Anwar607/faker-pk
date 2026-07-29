from faker_pk import FakerPK
from faker_pk.utils import query_value

def test_institution_filtered_by_level(faker_pk: FakerPK):
    inst = faker_pk.institution(level="university")
    assert isinstance(inst, str)
    inst_type = query_value("SELECT type FROM institutions WHERE name = ?", (inst,))
    assert inst_type == "university"
