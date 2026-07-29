import os
import pytest
from faker_pk.utils import query_value


class TestCNICGender:
    """Verify CNIC last digit aligns with gender."""

    def test_male_cnic_ends_odd(self, faker_pk):
        for _ in range(50):
            c = faker_pk.cnic(gender='male')
            last_digit = int(c[-1])
            assert last_digit % 2 == 1, f"Male CNIC should end odd, got {c}"

    def test_female_cnic_ends_even(self, faker_pk):
        for _ in range(50):
            c = faker_pk.cnic(gender='female')
            last_digit = int(c[-1])
            assert last_digit % 2 == 0, f"Female CNIC should end even, got {c}"

    def test_shorthand_gender_m(self, faker_pk):
        for _ in range(20):
            c = faker_pk.cnic(gender='m')
            assert int(c[-1]) % 2 == 1

    def test_shorthand_gender_f(self, faker_pk):
        for _ in range(20):
            c = faker_pk.cnic(gender='f')
            assert int(c[-1]) % 2 == 0

    def test_no_gender_still_valid(self, faker_pk):
        c = faker_pk.cnic()
        assert isinstance(c, str)
        assert len(c) == 15


class TestAddressConsistency:
    """Verify city, province, and postal code combinations are realistic."""

    def test_city_filtered_by_province(self, faker_pk):
        city = faker_pk.city(province="Sindh")
        # Verify this city actually belongs to Sindh in the DB
        province = query_value(
            "SELECT province FROM locations WHERE city = ?", (city,)
        )
        assert province == "Sindh"

    def test_province_for_known_city(self, faker_pk):
        province = faker_pk.province(city="Lahore")
        assert province == "Punjab"

    def test_full_address_with_city(self, faker_pk):
        addr = faker_pk.full_address(city="Karachi")
        assert "Karachi" in addr
        assert "Sindh" in addr
        assert "74000" in addr

    def test_full_address_with_province(self, faker_pk):
        addr = faker_pk.full_address(province="Balochistan")
        assert "Balochistan" in addr
        # Verify the city in the address actually belongs to Balochistan
        balochistan_cities = query_value(
            "SELECT city FROM locations WHERE province = 'Balochistan' AND ? LIKE '%' || city || '%'",
            (addr,)
        )
        assert balochistan_cities is not None


class TestBankIBAN:
    """Verify IBAN contains the correct bank identifier code."""

    def test_iban_with_specific_bank(self, faker_pk):
        iban_code = query_value(
            "SELECT iban_code FROM banks WHERE name = ?", ("Meezan Bank",)
        )
        iban = faker_pk.iban(bank="Meezan Bank")
        assert iban.startswith("PK")
        assert iban_code in iban

    def test_iban_format(self, faker_pk):
        iban = faker_pk.iban()
        assert iban.startswith("PK")
        assert len(iban) > 10

    def test_invalid_bank_raises(self, faker_pk):
        with pytest.raises(ValueError):
            faker_pk.iban(bank="Nonexistent Bank")


class TestPhoneProvider:
    """Verify phone numbers use correct provider prefixes."""

    def test_phone_with_specific_provider(self, faker_pk):
        from faker_pk.utils import query_list
        zong_prefixes = query_list(
            "SELECT prefix FROM sim_prefixes WHERE provider_name = ?", ("Zong",)
        )
        phone = faker_pk.phone_number(provider="Zong")
        # Strip +92, the next 3 digits should be a Zong prefix
        prefix = phone[3:6]
        assert prefix in zong_prefixes, f"Prefix {prefix} not in Zong prefixes"

    def test_invalid_provider_raises(self, faker_pk):
        with pytest.raises(ValueError):
            faker_pk.phone_number(provider="NonexistentProvider")


class TestCompanyIndustry:
    """Verify company names filter correctly by industry."""

    def test_company_filtered_by_industry(self, faker_pk):
        company = faker_pk.company_name(industry="IT")
        # Verify this company actually belongs to IT in the DB
        industry_code = query_value(
            "SELECT industry_code FROM companies WHERE name = ?", (company,)
        )
        assert industry_code == "IT"

    def test_invalid_industry_raises(self, faker_pk):
        with pytest.raises(ValueError):
            faker_pk.company_name(industry="FakeIndustry")


class TestAutoInitialization:
    """Verify the database auto-creates if the .db file is missing."""

    def test_db_recreates_at_new_path(self, tmp_path):
        import faker_pk.utils as utils_module

        test_db_path = str(tmp_path / "faker_pk.db")
        original_path = utils_module.DB_PATH

        try:
            # Point utils to a path where no DB exists
            utils_module.DB_PATH = test_db_path
            utils_module._db_initialized = False

            # Confirm no DB exists yet
            assert not os.path.exists(test_db_path)

            # This query should trigger auto-initialization
            result = utils_module.query_value("SELECT COUNT(*) FROM names")
            assert result is not None
            assert result > 0
            assert os.path.exists(test_db_path)
        finally:
            # Restore original path and reset flag
            utils_module.DB_PATH = original_path
            utils_module._db_initialized = False