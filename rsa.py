def input_integer(s):
    try:
        n = int(input(f"{s}>"))
        return n
    except ValueError:
        print("Integer Only!")
        exit(0)


def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)


def solve_public_key():
    p = input_integer("p:")
    q = input_integer("q:")
    n = p * q
    w = (p - 1) * (q - 1)
    e = 0
    for i in range(2, 1000000):
        if gcd(w, i) == 1:
            e = i
            break
    print("\nPublic Key")
    print(f"n:{n}\ne:{e}")
    solve_secret_key(p, q, w, n, e)


def solve_secret_key(p, q, w, n, e):
    d = 1
    for i in range(1, 100000 * w, w):
        if i % e == 0:
            d = i // e
            break
    print("\nSecret Key")
    print(f"n:{n}\nd:{d}")
    encrypt(n, e)
    decrypt(n, d)


def encrypt(n, e):
    print()
    m = input_integer("M:")
    c = m ** e % n
    print("\nEncryption")
    print(f"C:{c}")


def decrypt(n, d):
    print()
    c = input_integer("C:")
    m = c ** d % n
    print("\nDecryption")
    print(f"M:{m}")


if __name__ == '__main__':
    solve_public_key()
