import itertools
import math


def prime(n: int) -> int:
    if n < 1:
        raise ValueError("there is no zeroth prime")

    primes: list[int] = []
    for candidate in itertools.chain([2], itertools.count(3, 2)):
        limit = math.isqrt(candidate)
        if all(candidate % p != 0 for p in itertools.takewhile(lambda x: x <= limit, primes)):
            primes.append(candidate)
            if len(primes) == n:
                return candidate