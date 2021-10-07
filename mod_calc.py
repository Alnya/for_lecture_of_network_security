def best_mod_calc(n, _max, _mul, _sum, ls):
    if n == 1:
        for i in range(1, 14):
            _mul_tmp = _mul
            _sum_tmp = _sum
            _mul_tmp *= i
            _sum_tmp += i
            mod = _mul_tmp % _sum_tmp
            if _max < mod:
                _max = mod
                ls[n] = i
        return _max, ls
    for i in range(1, 14):
        mod, ls = best_mod_calc(n - 1, _max, _mul * i, _sum + i, ls)
        if _max < mod:
            _max = mod
            ls[n] = i
    return _max, ls


def main():
    for i in range(2, 10):
        mod, ls = best_mod_calc(i, 0, 1, 0, [0] * (i + 1))
        print(f"{i} : {mod} {ls[1:]}")


if __name__ == '__main__':
    main()
