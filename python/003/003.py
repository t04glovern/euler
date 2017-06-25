"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n = n / d
        d = d + 1

    return factors


primes = prime_factors(600851475143)
for item in primes:
    print(item)
