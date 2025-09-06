import itertools
import math


def prime(n: int) -> int:
    if n < 1:
        raise ValueError("there is no zeroth prime")

    primes: list[int] = []
    for candidate in itertools.chain([2], itertools.count(3, 2)):
     if all(candidate % p != 0 for p in primes if p <= math.isqrt(candidate)):
         if len(primes) < n:
             primes.append(candidate)
         else:
             return primes[-1]            