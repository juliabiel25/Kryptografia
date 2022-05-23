from random import randint

def gcd(p, q):
    while q != 0:
        p, q = q, p%q
    return p

def coprime(x, y):
    return gcd(x, y) == 1

def generate_value(p, q, n):
    if p > 0 and q > 0:
        x = 0
        while not coprime(n, x):
            x = randint(0, n)
        return x ** 2 % n


def generate(num, p, q, n):
    if p == q:
        print("error: p == q")
        return False

    if n == 0:
        print("error: n == 0")
        return False

    arr = []
    num += 1

    for i in range(num):
        generated = generate_value(p, q, n)
        arr.append(generated % 2)

    return arr


p = 0
q = 0
n = 0
generated_values = generate(10, p, q, n)
