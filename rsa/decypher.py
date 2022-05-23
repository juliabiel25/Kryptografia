def decypher(msg, key):
    d = key[0]
    n = key[1]

    print(f'd: {d}, n: {n}')

    # m = wiadomość zaszyfrowana ^ e mod n
    # m = ""
    # for c in msg:
    #     m += chr(ord(c)**d % n)

    m = ""
    for c in msg:
        print(pow(c, d, n))
        # m += chr(c ** d % n)

    return (m)