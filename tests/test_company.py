from faker_pk import FakerPK


def test_company_name(faker_pk: FakerPK) -> None:
    c: str = faker_pk.company_name()
    assert isinstance(c, str)
    assert len(c) > 0

def test_bank_name(faker_pk: FakerPK):
    b = faker_pk.bank_name()
    assert isinstance(b, str)
    assert len(b) > 0

def test_iban(faker_pk: FakerPK):
    i = faker_pk.iban()
    assert isinstance(i, str)
    assert i.startswith("PK")

def test_salary(faker_pk: FakerPK):
    s = faker_pk.salary()
    assert isinstance(s, int)
    assert s > 0

def test_job_title(faker_pk: FakerPK):
    j = faker_pk.job_title()
    assert isinstance(j, str)
    assert len(j) > 0

def test_industry_name(faker_pk: FakerPK):
    i = faker_pk.industry_name()
    assert isinstance(i, str)
    assert len(i) > 0

def test_job_title_with_industry(faker_pk: FakerPK):
    j = faker_pk.job_title_with_industry()
    assert isinstance(j, str)
    assert len(j) > 0
    assert " - " in j   
    