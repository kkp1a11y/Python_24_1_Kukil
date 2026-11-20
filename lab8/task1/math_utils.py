def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('Число не може бути від’ємним')
    return 1 if n < 2 else n * factorial(n - 1)


def is_prime(n: int) -> bool:
    if n < 2:
        raise ValueError('Число має бути не меншим за 2')
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def clamp(value: float, lo: float, hi: float) -> float:
    if lo > hi:
        raise ValueError('Нижня межа перевищує верхню')
    return max(lo, min(value, hi))
