"""A set of utilities related to prime numbers."""
import math


def primes_under(x):
    """Return a list of all primes under x. This is a basic implementation of
    the sieve of Eratosthenes, with no optimizations."""
    primes = []
    nums = [True] * (x + 1)
    for i in xrange(2, x):
        n = nums[i]
        if not n:
            continue
        d = x / i
        for j in xrange(2, d + 1):
            # mark each multiple of i as non-prime
            nums[j * i] = False
        primes.append(i)
    return primes

def primes_under_2(x):
    """Optimizations added."""
    if x < 3:
        return []
    # work directly on our list of primes
    nums = range(3, x, 2)
    # only eliminate non-primes until the square root of x
    root = int(math.ceil(x ** .5))
    # assume 2 is a prime and skip all evens
    for ii, i in enumerate(xrange(3, root, 2)):
        n = nums[ii]
        if not n:
            continue
        # if i is prime, all non-primes under i^2 should already be
        # eliminated, since they have to be factors of primes lower than i
        for j in xrange(i ** 2, x, i * 2):
            nums[(j / 2) - 1] = False
    # make sure our list includes 2 and knock out all non-primes
    return [2] + [n for n in nums if n]

def primes_under_3(x):
    """Implementing the optimization described here:
    http://codereview.stackexchange.com/a/7342"""
    nums = [True] * (x / 2)
    i = 5
    t = 2
    while i < x:
        if nums[i / 3]:
            nums[i / 3] = i
            j = i ** 2
            v = t
            while j < x:
                nums[j / 3] = False
                j += v * i
                v = 6 - v # alternate 2,4,2,4...
        i += t
        t = 6 - t # alternate 2,4,2,4...
    return [2, 3] + [n for n in nums if type(n) == int]
