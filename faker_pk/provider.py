from faker.providers import BaseProvider
from .personal import male_name, female_name, cnic, phone_number, sim_provider, caste, sect, dob
from .address import city, province, full_address
from .company import company_name, industry_name, job_title, job_title_with_industry, salary, bank_name, iban
from .education import institution, student_dob, student_profile

class FakerPKProvider(BaseProvider):
    """Faker provider for Pakistani personal info, addresses, companies, jobs, and more."""

    def _generate_multiple(self, func, count, **kwargs):
        """Generate one or many values based on count."""
        if count == 1:
            return func(**kwargs)
        return [func(**kwargs) for _ in range(count)]

    # --------------------
    # Personal Info
    # --------------------
    def pk_male_name(self, count=1):
        return self._generate_multiple(male_name, count)

    def pk_female_name(self, count=1):
        return self._generate_multiple(female_name, count)

    def pk_cnic(self, count=1, gender=None):
        return self._generate_multiple(cnic, count, gender=gender)

    def pk_phone_number(self, count=1, provider=None):
        return self._generate_multiple(phone_number, count, provider=provider)

    def pk_sim_provider(self, count=1):
        return self._generate_multiple(sim_provider, count)

    def pk_caste(self, count=1):
        return self._generate_multiple(caste, count)

    def pk_sect(self, count=1):
        return self._generate_multiple(sect, count)

    def pk_dob(self, count=1):
        return self._generate_multiple(dob, count)

    # --------------------
    # Address Info
    # --------------------
    def pk_city(self, count=1, province=None):
        return self._generate_multiple(city, count, province=province)

    def pk_province(self, count=1, city=None):
        return self._generate_multiple(province, count, city=city)

    def pk_full_address(self, count=1, city=None, province=None):
        return self._generate_multiple(full_address, count, city=city, province=province)

    # --------------------
    # Company Info
    # --------------------
    def pk_company_name(self, count=1, industry=None):
        return self._generate_multiple(company_name, count, industry=industry)

    def pk_industry_name(self, count=1):
        return self._generate_multiple(industry_name, count)

    def pk_bank_name(self, count=1):
        return self._generate_multiple(bank_name, count)

    def pk_iban(self, count=1, bank=None):
        return self._generate_multiple(iban, count, bank=bank)

    # --------------------
    # Job Info
    # --------------------
    def pk_job_title(self, count=1, industry=None):
        return self._generate_multiple(job_title, count, industry=industry)

    def pk_job_title_with_industry(self, count=1):
        return self._generate_multiple(job_title_with_industry, count)

    def pk_salary(self, count=1, industry=None):
        return self._generate_multiple(salary, count, industry=industry)
    # --------------------
    # Institution Info
    # --------------------
    def institution(self, count=1, level=None, city=None, province=None):
        return self._generate_multiple(institution, count, level=level, city=city, province=province)

    def student_profile(self, count=1, level=None, province=None):
        return self._generate_multiple(student_profile, count, level=level, province=province)
    