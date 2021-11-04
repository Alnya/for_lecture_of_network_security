def main():
    p = int(input("p:>>"))
    g = int(input("g:>>"))
    x = int(input("x:>>"))
    y = int(input("y:>>"))
    m = (g ** x) % p
    n = (g ** y) % p
    x_k = (n ** x) % p
    y_k = (m ** y) % p
    print(f"m:{m}\nn:{n}\nk:{x_k}, {y_k}")


if __name__ == '__main__':
    main()
