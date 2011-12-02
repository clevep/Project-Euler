"""A set of utilities related to prime numbers."""


def primes_under(x):
    """Return a list of all primes under x. Utilizes a basic sieve of
    Eratosthenes."""
    primes = []
    nums = [True] * x
    for i in xrange(2, x):
        n = nums[i]
        if not n:
            continue
        d = x / i
        for j in xrange(2, d + 1):
            nums[j * i] = False
        primes.append(i)
    return primes
