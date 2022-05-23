from sympy import prime, nextprime

def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1
    # return gcd(x, y) and is_prime(x) == 1


def generate_coprime(x):
    y = prime(1)
    while not is_coprime(x, y):
        y = nextprime(y)
    return y

