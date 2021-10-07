def all_attack():
    s = input("str:>")
    for i in range(26):
        for ss in s:
            if ss is " ":
                print(" ", end="")
                continue
            tmp = chr(ord('A') + (i + ord(ss)) % 26)
            print(tmp, end="")
        print()


if __name__ == '__main__':
    all_attack()
