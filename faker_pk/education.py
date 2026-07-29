import random
from datetime import date, timedelta
from .utils import query_value, query_row


# Age ranges per institution level
AGE_RANGES = {
    "school":     (5, 14),
    "college":    (14, 18),
    "university": (18, 25)
}


def institution(level=None, city=None, province=None):
    """Return a random institution name, optionally filtered by level, city, or province."""
    conditions = []
    params = []

    if level:
        conditions.append("i.type = ?")
        params.append(level.lower())
    if city:
        conditions.append("i.city = ?")
        params.append(city)
    if province:
        conditions.append("l.province = ?")
        params.append(province)

    where = f"WHERE {' AND '.join(conditions)}" if conditions else ""

    query = f"""
        SELECT i.name FROM institutions i
        JOIN locations l ON i.city = l.city
        {where}
        ORDER BY RANDOM() LIMIT 1
    """
    return query_value(query, tuple(params))


def student_dob(level="university"):
    """Generate an age-appropriate DOB for a student at the given level."""
    if level:
        level = level.lower()
    min_age, max_age = AGE_RANGES.get(level, (18, 25))
    today = date.today()
    start = today.replace(year=today.year - max_age)
    end = today.replace(year=today.year - min_age)
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))


def student_profile(level=None, province=None):
    """Generate a complete, coherent student profile.

    Returns a dict with name, gender, cnic, institution, city, province, dob.
    All fields are consistent (institution matches city/province, dob matches level).
    """
    from .personal import male_name, female_name, cnic

    # Default to random level if not specified
    if not level:
        level = random.choice(["school", "college", "university"])
    else:
        level = level.lower()

    # Pick a random institution, optionally in the given province
    conditions = ["i.type = ?"]
    params = [level]
    if province:
        conditions.append("l.province = ?")
        params.append(province)

    where = f"WHERE {' AND '.join(conditions)}"
    row = query_row(f"""
        SELECT i.name, i.city, l.province FROM institutions i
        JOIN locations l ON i.city = l.city
        {where}
        ORDER BY RANDOM() LIMIT 1
    """, tuple(params))

    if not row:
        raise ValueError(f"No institution found for level='{level}', province='{province}'")

    inst_name, city_name, province_name = row

    # Generate gender-consistent personal data
    gender = random.choice(["male", "female"])
    name = male_name() if gender == "male" else female_name()

    return {
        "name": name,
        "gender": gender,
        "cnic": cnic(gender=gender),
        "institution": inst_name,
        "level": level,
        "city": city_name,
        "province": province_name,
        "dob": student_dob(level)
    }