def prime(n):
    """Calculate nth prime number."""
    if n < 1:
        raise ValueError("there is no zeroth prime")

    counter = 0
    candidate = 2
    while True:
        if _is_prime(candidate):
            counter += 1
        if counter == n:
            return candidate
        candidate += 1
            

def _is_prime(n):
    """Check if number is prime or not."""
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True