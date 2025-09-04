import itertools
import math


def prime(n):
    if n < 1:
        raise ValueError("there is no zeroth prime")

    primes = []
    for candidate in itertools.chain([2], itertools.count(3, 2)):
       if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
            if len(primes) == n:
                return candidate