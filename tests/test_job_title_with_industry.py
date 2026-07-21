from faker_pk import FakerPK

def test_job_title_with_industry(faker_pk: FakerPK):
    j = faker_pk.job_title_with_industry()
    assert isinstance(j, str)
    assert len(j) > 0
    assert " - " in j
