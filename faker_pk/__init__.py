from .personal import male_name, female_name, cnic, phone_number, sim_provider, caste, sect, dob
from .address import city, province, full_address
from .company import company_name, industry_name, iban, bank_name, salary, job_title_with_industry, job_title
from .provider import FakerPKProvider
from .education import institution, student_dob, student_profile



class FakerPK:
    """Generate fake Pakistani names, addresses, CNICs, phone numbers, and more."""

    def _generate_multiple(self, func, count, **kwargs):
        """Generate one or many values based on count."""
        if count == 1:
            return func(**kwargs)
        return [func(**kwargs) for _ in range(count)]

    # --------------------
    # Personal Info
    # --------------------
    def male_name(self, count=1):
        return self._generate_multiple(male_name, count)

    def female_name(self, count=1):
        return self._generate_multiple(female_name, count)

    def cnic(self, count=1, gender=None):
        return self._generate_multiple(cnic, count, gender=gender)

    def phone_number(self, count=1, provider=None):
        return self._generate_multiple(phone_number, count, provider=provider)

    def sim_provider(self, count=1):
        return self._generate_multiple(sim_provider, count)

    def caste(self, count=1):
        return self._generate_multiple(caste, count)

    def sect(self, count=1):
        return self._generate_multiple(sect, count)

    def dob(self, count=1):
        return self._generate_multiple(dob, count)

    # --------------------
    # Address Info
    # --------------------
    def city(self, count=1, province=None):
        return self._generate_multiple(city, count, province=province)

    def province(self, count=1, city=None):
        return self._generate_multiple(province, count, city=city)

    def full_address(self, count=1, city=None, province=None):
        return self._generate_multiple(full_address, count, city=city, province=province)

    # --------------------
    # Company Info
    # --------------------
    def company_name(self, count=1, industry=None):
        return self._generate_multiple(company_name, count, industry=industry)

    def industry_name(self, count=1):
        return self._generate_multiple(industry_name, count)

    def bank_name(self, count=1):
        return self._generate_multiple(bank_name, count)

    def iban(self, count=1, bank=None):
        return self._generate_multiple(iban, count, bank=bank)

    # --------------------
    # Job Info
    # --------------------
    def job_title(self, count=1, industry=None):
        return self._generate_multiple(job_title, count, industry=industry)

    def job_title_with_industry(self, count=1):
        return self._generate_multiple(job_title_with_industry, count)

    def salary(self, count=1, industry=None):
        return self._generate_multiple(salary, count, industry=industry)
    
    # --------------------
    # Institution Info
    # --------------------
    def institution(self, count=1, level=None, city=None, province=None):
        return self._generate_multiple(institution, count, level=level, city=city, province=province)

    def student_profile(self, count=1, level=None, province=None):
        return self._generate_multiple(student_profile, count, level=level, province=province)
    
__all__ = ["FakerPK", "FakerPKProvider"]