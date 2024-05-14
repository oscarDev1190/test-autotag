class Calculator:
    def sum(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        if b != 0:
            return a / b

    def sqrt(n):
        import math

        if n >= 0:
            return math.sqrt(n)
