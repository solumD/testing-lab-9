class Calculator:
    """Калькулятор для лабораторной работы по модульному тестированию."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("деление на ноль")
        return a / b

    def is_prime_number(self, number: int) -> bool:
        if number < 2:
            return False

        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                return False
            divisor += 1
        return True
