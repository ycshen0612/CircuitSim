import math


class Point(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __call__(self):
        return self.x, self.y

    def reset(self, x=None, y=None):
        if x is not None:
            self.x = x
        else:
            self.x = 0

        if y is not None:
            self.y = y
        else:
            self.y = 0

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y)


class Complex(object):
    def __init__(self, real=None, imag=None):
        self.real = real
        self.imag = imag

    def __call__(self, *args, **kwargs):
        return self.real, self.imag

    def __str__(self):
        return "{} + {}i".format(self.real, self.imag)

    def __add__(self, other):
        return Complex(real=self.real + other.real, imag=self.imag + other.imag)

    def __sub__(self, other):
        return Complex(real=self.real - other.real, imag=self.imag - other.imag)

    def __mul__(self, other):
        return Complex(real=(self.real * other.real) - (self.imag * other.imag),
                       imag=(self.imag * other.imag) + (self.real * self.imag))

    def __truediv__(self, other):
        div = other.real ** 2 + other.imag ** 2
        return Complex(real=((self.real * other.real) + (self.imag * other.imag)) / div,
                       imag=((self.imag * other.imag) - (self.real * self.imag)) / div)

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)
