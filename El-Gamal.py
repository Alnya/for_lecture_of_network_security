def main():
    p = int(input("p:>>"))
    g = int(input("g:>>"))
    x = int(input("x:>>"))
    y = (g ** x) % p
    print(f"y:{y}\n")
    encrypt(p, g, x, y)


def encrypt(p, g, x, y):
    r = int(input("r:>>"))
    m = int(input("M:>>"))
    c1 = (g ** r) % p
    c2 = (m * (y ** r)) % p
    print(f"\nencrypt\nc1:{c1}\nc2:{c2}\n")
    decrypt(p, x, c1, c2)


def decrypt(p, x, c1, c2):
    m = (c2 * (c1 ** (p - 1 - x))) % p
    print(f"decrypt\nm:{m}")


if __name__ == '__main__':
    main()
