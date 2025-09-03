import itertools


def prime_generator():
    """Generate primes indefinitely"""
    primes = []
    candidate = 2
    while True:
        is_p = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_p = False
                break
        if is_p:
            primes.append(candidate)
            yield candidate
        candidate += 1 if candidate == 2 else 2


def prime(n):
    """Calculate nth prime"""
    if n < 1:
        raise ValueError("there is no zeroth prime")
    return next(itertools.islice(prime_generator(), n - 1, n))