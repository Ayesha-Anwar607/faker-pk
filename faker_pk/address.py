import random
from .utils import query_value, query_row


def city(province=None):
    """Return a random Pakistani city. Optionally filter by province."""
    if province:
        return query_value(
            "SELECT city FROM locations WHERE province = ? ORDER BY RANDOM() LIMIT 1",
            (province,)
        )
    return query_value("SELECT city FROM locations ORDER BY RANDOM() LIMIT 1")


def province(city=None):
    """Return a random province. If city is given, return its matching province."""
    if city:
        return query_value(
            "SELECT province FROM locations WHERE city = ? LIMIT 1", (city,)
        )
    return query_value("SELECT province FROM locations ORDER BY RANDOM() LIMIT 1")


def full_address(city=None, province=None):
    """Generate a realistic full Pakistani address with real postal code."""
    if city:
        row = query_row(
            "SELECT city, province, postal_code FROM locations WHERE city = ? LIMIT 1",
            (city,)
        )
    elif province:
        row = query_row(
            "SELECT city, province, postal_code FROM locations WHERE province = ? ORDER BY RANDOM() LIMIT 1",
            (province,)
        )
    else:
        row = query_row(
            "SELECT city, province, postal_code FROM locations ORDER BY RANDOM() LIMIT 1"
        )

    city_name, province_name, postal_code = row
    house_no = f"House No. {random.randint(1, 999)}"
    street = f"Street No. {random.randint(1, 30)}"
    return f"{house_no}, {street}, {city_name}, {province_name}, {postal_code}"