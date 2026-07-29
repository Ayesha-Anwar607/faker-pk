import random
from datetime import date, timedelta
from .utils import query_value, query_list


def sim_provider():
    """Return a random SIM provider name."""
    return query_value("SELECT name FROM sim_providers ORDER BY RANDOM() LIMIT 1")


def caste():
    """Return a random caste name."""
    return query_value("SELECT name FROM castes ORDER BY RANDOM() LIMIT 1")


def sect():
    """Return a random sect name."""
    return query_value("SELECT name FROM sects ORDER BY RANDOM() LIMIT 1")


def dob(start_year=1950, end_year=2006):
    """Generate a random date of birth between start_year and end_year."""
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def male_name():
    """Generate a random male full name."""
    first = query_value("SELECT name FROM names WHERE type = 'male' ORDER BY RANDOM() LIMIT 1")
    last = query_value("SELECT name FROM names WHERE type = 'last' ORDER BY RANDOM() LIMIT 1")
    return f"{first} {last}"


def female_name():
    """Generate a random female full name."""
    first = query_value("SELECT name FROM names WHERE type = 'female' ORDER BY RANDOM() LIMIT 1")
    last = query_value("SELECT name FROM names WHERE type = 'last' ORDER BY RANDOM() LIMIT 1")
    return f"{first} {last}"


def cnic(gender=None):
    """Generate a random CNIC.
    If gender is 'male' or 'm', the last digit is odd.
    If gender is 'female' or 'f', the last digit is even.
    """
    part1 = str(random.randint(10000, 99999))
    part2 = str(random.randint(1000000, 9999999))

    if gender and gender.lower() in ('male', 'm'):
        part3 = str(random.choice([1, 3, 5, 7, 9]))
    elif gender and gender.lower() in ('female', 'f'):
        part3 = str(random.choice([0, 2, 4, 6, 8]))
    else:
        part3 = str(random.randint(0, 9))

    return f"{part1}-{part2}-{part3}"


def phone_number(provider=None):
    """Generate a random Pakistani phone number.
    If provider is specified, use that provider's prefixes only.
    """
    if provider:
        prefixes = query_list(
            "SELECT prefix FROM sim_prefixes WHERE provider_name = ?", (provider,)
        )
        if not prefixes:
            raise ValueError(f"SIM provider '{provider}' not found.")
    else:
        prefixes = query_list("SELECT prefix FROM sim_prefixes")

    prefix = random.choice(prefixes)
    remaining = str(random.randint(1000000, 9999999))
    return f"+92{prefix}{remaining}"