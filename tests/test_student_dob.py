from datetime import date
from faker_pk.education import student_dob

def test_student_dob_age_ranges():
    today = date.today()

    for _ in range(20):
        dob = student_dob(level="school")
        age = (today - dob).days // 365
        assert 5 <= age <= 14

    for _ in range(20):
        dob = student_dob(level="college")
        age = (today - dob).days // 365
        assert 14 <= age <= 18

    for _ in range(20):
        dob = student_dob(level="university")
        age = (today - dob).days // 365
        assert 18 <= age <= 25
