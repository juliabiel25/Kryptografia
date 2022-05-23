from gen_coprime import generate_coprime
from sympy import randprime, prime, nextprime


def generate_keys():
    # wybierz różne liczby pierwsze p i q
    p = randprime(1000, 9999)
    q = randprime(1000, 9999)
    while q == p:
        q = randprime(1000, 9999)

    # p = 31
    # q = 19
    print(f'p: {p}\nq: {q}')

    n = p * q
    phi = (p - 1) * (q - 1)
    print(f'n: {n}\nphi: {phi}')

    # wygeneruj liczbę względnie pierwszą z phi
    e = generate_coprime(phi)
    print(f'e: {e}')

    # wygeneruj d spełniające warunek e * d przystaje do 1 mod phi
    d = 1
    while (e * d - 1) % phi != 0:
        d += 1
    print(f'd: {d}')

    print(f'\nklucz publiczny: {e}, {n}')
    print(f'klucz prywatny: {d}, {n}')
    return (e, n), (d, n)

