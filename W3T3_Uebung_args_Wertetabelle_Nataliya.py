def quadrat(x):
    return x ** 2


def mult(x):
    return x * 10000000000


def wertetabelle(fkt, von, bis):
    max_len_left = 0
    max_len_right = 0
    for i in range(von, bis + 1):
        if len(str(i)) > max_len_left:
            max_len_left = len(str(i)) + 2
        if len(str(fkt(i))) > max_len_right:
            max_len_right = len(str(fkt(i))) + 2

    x, y, dash = "x", "y", "-"
    print(f"{x:^{max_len_left}}|{y:^{max_len_right}}")
    print(f"{dash * max_len_left}+{dash * max_len_right}")
    for i in range(von, bis + 1):
        print(f"{i:^{max_len_left}}|{fkt(i):^{max_len_right}}")


if __name__ == "__main__":
    wertetabelle(quadrat, 30000, 30005)
    wertetabelle(mult, 1, 5)
