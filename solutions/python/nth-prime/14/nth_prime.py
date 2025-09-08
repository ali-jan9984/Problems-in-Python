import math


def prime(n: int) -> int:
    if n < 1:
        raise ValueError("there is no zeroth prime")
    if n == 1:
        return 2
        
    #set the limit to 15 if n < 6, otherwise it will calculate limit using the formula
    limit = 15 if n < 6 else int(n * (math.log(n) + math.log(math.log(n)))) + 10

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