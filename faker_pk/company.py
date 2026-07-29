import random
from .utils import query_value, query_row


def _normalize_industry(industry):
    """Map a human-readable industry name to its internal code.
    Accepts both full names ('Information Technology') and codes ('IT').
    """
    # Check if it's already a valid code
    code = query_value("SELECT code FROM industries WHERE code = ?", (industry,))
    if code:
        return code
    # Try mapping from full name
    code = query_value("SELECT code FROM industries WHERE name = ?", (industry,))
    if code:
        return code
    raise ValueError(f"Industry '{industry}' not found.")


def bank_name():
    """Return a random Pakistani bank name."""
    return query_value("SELECT name FROM banks ORDER BY RANDOM() LIMIT 1")


def iban(bank=None):
    """Generate a realistic Pakistani IBAN.
    If bank is specified, use that bank's actual IBAN code.
    """
    if bank:
        code = query_value("SELECT iban_code FROM banks WHERE name = ?", (bank,))
        if not code:
            raise ValueError(f"Bank '{bank}' not found.")
    else:
        code = query_value("SELECT iban_code FROM banks ORDER BY RANDOM() LIMIT 1")

    checksum = str(random.randint(10, 99))
    account = str(random.randint(10**15, 10**16 - 1))
    return f"PK{checksum}{code}{account}"


def company_name(industry=None):
    """Return a random company name. Optionally filter by industry."""
    if industry:
        code = _normalize_industry(industry)
        return query_value(
            "SELECT name FROM companies WHERE industry_code = ? ORDER BY RANDOM() LIMIT 1",
            (code,)
        )
    return query_value("SELECT name FROM companies ORDER BY RANDOM() LIMIT 1")


def industry_name():
    """Return a random industry name (human-readable)."""
    return query_value("SELECT name FROM industries ORDER BY RANDOM() LIMIT 1")


def job_title(industry=None):
    """Return a random job title. Optionally filter by industry."""
    if industry:
        code = _normalize_industry(industry)
        return query_value(
            "SELECT title FROM job_titles WHERE industry_code = ? ORDER BY RANDOM() LIMIT 1",
            (code,)
        )
    return query_value("SELECT title FROM job_titles ORDER BY RANDOM() LIMIT 1")


def job_title_with_industry():
    """Return a string of 'job_title - industry_code'."""
    row = query_row("SELECT title, industry_code FROM job_titles ORDER BY RANDOM() LIMIT 1")
    return f"{row[0]} - {row[1]}"


def salary(industry=None):
    """Generate a random salary in PKR based on industry salary ranges, rounded to clean figures."""
    if industry:
        code = _normalize_industry(industry)
        row = query_row(
            "SELECT min_salary, max_salary FROM industries WHERE code = ?", (code,)
        )
        if row:
            raw_salary = random.randint(row[0], row[1])
            return round(raw_salary / 500) * 500

    row = query_row(
        "SELECT min_salary, max_salary FROM industries ORDER BY RANDOM() LIMIT 1"
    )
    raw_salary = random.randint(row[0], row[1])
    return round(raw_salary / 500) * 500