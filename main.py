from math import gcd


# hw 15.2
class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b
        self._reduce()  # Сокращение дроби при создании

    def _reduce(self):
        """Сокращает дробь до несократимой."""
        divisor = gcd(self.a, self.b)
        self.a //= divisor
        self.b //= divisor

    def __add__(self, other):
        """Сложение дробей."""
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        """Вычитание дробей."""
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __mul__(self, other):
        """Умножение дробей."""
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        """Сравнение на равенство."""
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        """Сравнение меньше."""
        return self.a * other.b < other.a * self.b

    def __gt__(self, other):
        """Сравнение больше."""
        return self.a * other.b > other.a * self.b

    def __str__(self):
        """Возвращает строковое представление дроби."""
        return f"Fraction: {self.a}, {self.b}"



try:
    f_a = Fraction(2, 3)
    f_b = Fraction(3, 6)
    print("f_a:", f_a)
    print("f_b:", f_b)

    f_c = f_b + f_a
    print("f_c (f_b + f_a):", f_c)
    assert str(f_c) == 'Fraction: 21, 18', f"Expected 'Fraction: 21, 18', got {str(f_c)}"

    f_d = f_b * f_a
    print("f_d (f_b * f_a):", f_d)
    assert str(f_d) == 'Fraction: 6, 18', f"Expected 'Fraction: 6, 18', got {str(f_d)}"

    f_e = f_a - f_b
    print("f_e (f_a - f_b):", f_e)
    assert str(f_e) == 'Fraction: 3, 18', f"Expected 'Fraction: 3, 18', got {str(f_e)}"

    assert f_d < f_c, f"f_d should be less than f_c"
    assert f_d > f_e, f"f_d should be greater than f_e"
    assert f_a != f_b, f"f_a should not equal f_b"

    f_1 = Fraction(2, 4)
    f_2 = Fraction(3, 6)
    print("f_1:", f_1)
    print("f_2:", f_2)
    assert f_1 == f_2, f"f_1 should equal f_2"

    print('All tests passed. OK')
except AssertionError as e:
    print("Test failed:", e)
except Exception as ex:
    print("Error:", ex)




