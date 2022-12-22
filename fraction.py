from math import gcd


class Fraction:
    def __init__(self, n: int | float | str = 0):
        self.whole_part = 0
        self.numerator = 0
        self.denominator = 1
        self.neg = str(n)[0] == '-'
        if isinstance(n, int):
            self.whole_part = n if str(n)[0] != '-' else -n
            self.numerator = 0
            self.denominator = 1
        if isinstance(n, (float, str)):
            s = str(n).split('.')
            self.whole_part = int(s[0]) if str(n)[0] != '-' else -int(s[0])
            self.numerator = int(s[1])
            self.denominator = 10 ** len(s[1])
        self.normalise()

    def __str__(self):
        return f'{"-(" if self.neg else ""}{self.whole_part}+({self.numerator}/{self.denominator}){")" if self.neg else ""}'

    def __int__(self):
        self.normalise()
        return self.whole_part * self.neg_to_multiplier

    def __float__(self):
        self.normalise()
        return (self.whole_part + (self.numerator / self.denominator)) * self.neg_to_multiplier

    def __add__(self, other):
        if not isinstance(other, (int, float, self.__class__)):
            raise TypeError(
                f'unsupported operand type(s) for +: \'{self.__class__.__name__}\' and \'{type(other).__name__}\'')
        if isinstance(other, (int, float)):
            other = Fraction(other)

        f = Fraction(0)
        self.denormalize()
        other.denormalize()
        g = self.denominator * other.denominator
        n = self.numerator * self.neg_to_multiplier * other.denominator + other.numerator * other.neg_to_multiplier * self.denominator
        if n < 0:
            f.neg = True
            n = -n
        f.numerator = n
        f.denominator = g
        f.normalise()
        return f

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (other.__neg__())

    def __mul__(self, other):
        self.denormalize()
        if isinstance(other, (int, float)):
            other = Fraction(other)

        if float(other) == -1.0:
            self.normalise()
            return -self

        other.denormalize()
        f = Fraction(0)
        f.numerator = self.numerator * other.numerator
        f.denominator = self.denominator * other.denominator
        f.neg = self.neg and other.neg
        f.normalise()
        return f

    def __rmul__(self, other):
        return self * other

    def inverse(self):
        a = self
        a.denormalize()
        a.numerator, a.denominator = a.denominator, a.numerator
        a.normalise()
        return a

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self * Fraction(other).inverse()
        if isinstance(other, Fraction):
            return self * other.inverse()

    def __pow__(self, power, modulo=None):
        f = self
        f.denormalize()
        s = Fraction(f.numerator ** float(power)) / Fraction(f.denominator ** float(power))
        s.normalise()
        return -s if f.neg else s

    @property
    def neg_to_multiplier(self):
        return -1 if self.neg else 1

    def normalise(self):
        self.whole_part += self.numerator // self.denominator
        self.numerator -= (self.numerator // self.denominator) * self.denominator
        self.nod()
        return self

    def denormalize(self):
        self.numerator += self.denominator * self.whole_part
        self.whole_part = 0
        return self

    def nod(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g
        return self

    def __neg__(self):
        self.neg = not self.neg
        return self
