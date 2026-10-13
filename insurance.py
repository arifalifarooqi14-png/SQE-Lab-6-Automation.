
def calculate_discount(age_group, claims, policy):
    """Calculate the insurance discount percentage."""

    # Two or more claims: no discount
    if claims == "2+":
        return 0

    # Exactly one claim
    if claims == "1":
        if policy == "Standard":
            return 5
        elif policy == "Premium":
            return 10

    # No claims
    if claims == "None":
        if age_group == "<25":
            return 10 if policy == "Standard" else 15

        elif age_group == "25-65":
            return 15 if policy == "Standard" else 20

        elif age_group == ">65":
            return 10 if policy == "Standard" else 15

    raise ValueError("Invalid insurance input")


def get_age_group(age):
    """Convert a numeric age into the Lab 4 age group."""

    if not isinstance(age, int) or isinstance(age, bool) or age < 1:
        raise ValueError("Age must be a positive integer")

    if age < 25:
        return "<25"
    elif age <= 65:
        return "25-65"
    else:
        return ">65"
