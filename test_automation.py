
import pytest

from triangle import classify_triangle
from insurance import calculate_discount, get_age_group


# ==========================================
# LAB 2: TRIANGLE CLASSIFIER TESTS
# ==========================================

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 3) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"


# ==========================================
# LAB 4: INSURANCE DISCOUNT TESTS
# ==========================================

def test_no_claims_standard_policy():
    age_group = get_age_group(40)
    actual = calculate_discount(
        age_group, "None", "Standard"
    )
    assert actual == 15


def test_no_claims_premium_policy():
    age_group = get_age_group(40)
    actual = calculate_discount(
        age_group, "None", "Premium"
    )
    assert actual == 20


def test_one_claim_standard_policy():
    age_group = get_age_group(30)
    actual = calculate_discount(
        age_group, "1", "Standard"
    )
    assert actual == 5


def test_two_or_more_claims():
    age_group = get_age_group(30)
    actual = calculate_discount(
        age_group, "2+", "Premium"
    )
    assert actual == 0
