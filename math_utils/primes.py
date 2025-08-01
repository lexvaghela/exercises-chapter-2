def isprime(n):
    """Returns if a number is prime or not."""
    from math import sqrt
    if n == 1:
        return False
    if n == 2:
        return True
    start = 2
    while start <= sqrt(n):
        if n % start == 0:
            return False
        start += 1
    return True
