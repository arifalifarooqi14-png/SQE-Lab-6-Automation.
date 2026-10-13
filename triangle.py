
def classify_triangle(a, b, c):
    """Classify a triangle using three integer sides."""

    sides = [a, b, c]

    # Check valid input range
    if any(not isinstance(x, int) or isinstance(x, bool)
           or x < 1 or x > 200 for x in sides):
        return "Invalid"

    # Check triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid"

    # Classify the triangle
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
