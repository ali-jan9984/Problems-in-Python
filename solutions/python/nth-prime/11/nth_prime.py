import itertools


def prime(n: int) -> int:
    if n < 1:
        raise ValueError("there is no zeroth prime")

    primes: list[int] = []
    for candidate in itertools.chain([2], itertools.count(3, 2)):
        if all(
            candidate % p != 0
            for p in itertools.takewhile(lambda x: x * x <= candidate, primes)
        ):
            if len(primes) == n:
                return primes[-1]
            primes.append(candidate)