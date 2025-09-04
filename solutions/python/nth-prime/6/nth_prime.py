import itertools
import math


def prime(n):
    if n < 1:
        raise ValueError("there is no zeroth prime")

    primes = []
    candidate_iter = itertools.chain([2], itertools.count(3, 2))
    for candidate in candidate_iter:
        for p in primes:
            if candidate % p == 0:
                break
        else:
            primes.append(candidate)
            if len(primes) == n: return candidate