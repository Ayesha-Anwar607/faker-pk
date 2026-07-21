from faker_pk import FakerPK

def test_job_title(faker_pk: FakerPK):
    j = faker_pk.job_title()
    assert isinstance(j, str)
    assert len(j) > 0
