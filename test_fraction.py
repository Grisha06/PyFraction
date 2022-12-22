import unittest

from fraction import *


class TestFraction(unittest.TestCase):
    def test_float(self):
        self.assertEqual(float(Fraction(1.15)), 1.15, "Float conversion error")

    def test_int(self):
        self.assertEqual(int(Fraction(1.15)), 1, "Int conversion error")

    def test_str(self):
        self.assertEqual(str(Fraction(1.15)) + str(Fraction(-1.15)), '1+(3/20)-(1+(3/20))', "String conversion error")

    def test_sum_self(self):
        self.assertEqual(float(Fraction(1.15) + Fraction(-1.15)), 0.0, "Sum with fraction error")

    def test_sum_int(self):
        self.assertEqual(float(Fraction(1.15) + -1), 0.15, "Sum with int error")

    def test_sum_float(self):
        self.assertEqual(float(Fraction(1.15) + -1.15), 0.0, "Sum with float error")

    def test_mul_self(self):
        self.assertEqual(float(Fraction(1.15) * Fraction(-1)), -1.15, "Multiple by fraction error")

    def test_mul_int(self):
        self.assertEqual(float(Fraction(1.15) * -1), -1.15, "Multiple by int error")

    def test_mul_float(self):
        self.assertEqual(float(Fraction(1.15) * -1.0), -1.15, "Multiple by float error")

    def test_div_self(self):
        self.assertEqual(float(Fraction(1.15) / Fraction(-1)), -1.15, "Multiple by fraction error")

    def test_div_int(self):
        self.assertEqual(float(Fraction(1.15) / -1), -1.15, "Multiple by int error")

    def test_div_float(self):
        self.assertEqual(float(Fraction(1.15) / -1.0), -1.15, "Multiple by float error")

    def test_pow_self(self):
        self.assertEqual(float(Fraction(2) ** Fraction(-1)), 0.5, "Power with fraction error")

    def test_pow_int(self):
        self.assertEqual(float(Fraction(2) ** -1), 0.5, "Power with int error")

    def test_pow_float(self):
        self.assertEqual(float(Fraction(2) ** -1.0), 0.5, "Power with float error")

    def test_sqrt_self(self):
        self.assertEqual(float(Fraction(4) ** Fraction(1 / 2)), 2, "Square root with fraction error")

    def test_sqrt_float(self):
        self.assertEqual(float(Fraction(4) ** (1 / 2)), 2, "Square root with float error")

    def test_num_root_self(self):
        self.assertEqual(float(Fraction(27) ** Fraction(1 / 3)), 3, "Num root with fraction error")

    def test_num_root_float(self):
        self.assertEqual(float(Fraction(27) ** (1 / 3)), 3, "Num root with float error")

    def test_inverse(self): self.assertEqual(float(Fraction(2).inverse()), 0.5, "Inverse error")

    def test_normalise_denormalize(self):
        self.assertEqual(float(Fraction(1.15).normalise().denormalize()), 1.15, "Normalise/Denormalize error")

    def test_neg_to_multiplier_positive(self):
        self.assertEqual(Fraction(1.15).neg_to_multiplier, 1, "Positive Neg to multiplier error")

    def test_neg_to_multiplier_negative(self):
        self.assertEqual(Fraction(-1.15).neg_to_multiplier, -1, "Negative Neg to multiplier error")


if __name__ == '__main__':
    unittest.main()
