from faker import Faker
import pytest
from faker_pk import FakerPKProvider, FakerPK

def test_faker_pk_provider_multiple_count():
    fake = Faker()
    fake.add_provider(FakerPKProvider)

    # Test count > 1 branches in provider.py
    assert len(fake.pk_male_name(count=2)) == 2
    assert len(fake.pk_female_name(count=2)) == 2
    assert len(fake.pk_cnic(count=2)) == 2
    assert len(fake.pk_phone_number(count=2)) == 2
    assert len(fake.pk_sim_provider(count=2)) == 2
    assert len(fake.pk_caste(count=2)) == 2
    assert len(fake.pk_sect(count=2)) == 2
    assert len(fake.pk_dob(count=2)) == 2
    assert len(fake.pk_city(count=2)) == 2
    assert len(fake.pk_province(count=2)) == 2
    assert len(fake.pk_full_address(count=2)) == 2
    assert len(fake.pk_company_name(count=2)) == 2
    assert len(fake.pk_industry_name(count=2)) == 2
    assert len(fake.pk_bank_name(count=2)) == 2
    assert len(fake.pk_iban(count=2)) == 2
    assert len(fake.pk_job_title(count=2)) == 2
    assert len(fake.pk_job_title_with_industry(count=2)) == 2
    assert len(fake.pk_salary(count=2)) == 2
    assert len(fake.institution(count=2)) == 2
    assert len(fake.student_profile(count=2)) == 2

def test_faker_pk_edge_cases():
    fpk = FakerPK()
    # Test invalid gender fallback in cnic
    assert fpk.cnic(gender="invalid") is not None
        # Test invalid industry raises ValueError
    with pytest.raises(ValueError):
        fpk.salary(industry="NonExistentIndustry")