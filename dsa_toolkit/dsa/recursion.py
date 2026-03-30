class Recursion:
    def factorial(self, n):
        if n < 0:
            raise ValueError("Number must be non-negative")
        if n in (0, 1):
            return 1
        return n * self.factorial(n - 1)
def fibonacci(self, n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    if n <= 1:
        return n
    return self.fibonacci(n - 1) + self.fibonacci(n - 2)
def power(self, base, exp):
    if exp < 0:
        raise ValueError("Exponent must be non-negative")
    if exp == 0:
        return 1
    return base * self.power(base, exp - 1)
def reverse_string(self, text):
    if len(text) <= 1:
        return text
    return text[-1] + self.reverse_string(text[:-1])
def sum_of_digits(self, n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    if n == 0:
        return 0
    return n % 10 + self.sum_of_digits(n // 10)