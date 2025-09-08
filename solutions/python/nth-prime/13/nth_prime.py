import math


def prime(n: int) -> int:
    if n < 1:
        raise ValueError("there is no zeroth prime")
    if n == 1:
        return 2

    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 10 #formula for calculating the best possible limit for nth prime

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, math.isqrt(limit) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    count = 0
    for i, is_prime in enumerate(sieve):
        if is_prime:
            count += 1
            if count == n:
                return i