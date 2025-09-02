from itertools import islice, count
import math


def prime(n):
    """Calculate nth prime number."""
    if n < 1:
        raise ValueError("there is no zeroth prime")
    gen = islice(filter(_is_prime, count(2)), n)
    for _ in range(n - 1): 
        next(gen)
    return next(gen)


def _is_prime(n):
    """Check if n is prime or not."""
    return all(n % i != 0 for i in range(2, math.isqrt(n) + 1))