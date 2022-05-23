from alphabet import code


def encypher(msg, key):
    msg = msg.lower()
    e = key[0]
    n = key[1]

    # c = wiadomość ^ e mod n
    # c = ""
    # for m in msg:
    #     c += chr(ord(m)**e % n))

    c = []
    for m in msg:
        c.append(code[m] ** e % n)
        # c.append(ord(m)**e % n)

    return (c)