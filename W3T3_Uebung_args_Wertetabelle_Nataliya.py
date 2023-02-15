def quadrat(x):
    return x ** 2


def mult(x):
    return x * 10000000000


def wertetabelle(fkt, von, bis):
    max_len_left = 0
    max_len_right = 0
    for i in range(von, bis + 1):
        if len(str(i)) >= max_len_left:
            max_len_left = len(str(i)) + 1
        if len(str(fkt(i))) >= max_len_right:
            max_len_right = len(str(fkt(i))) + 1
        print(len(str(fkt(i))))
    x, y, dash = "x", "y", "-"
    print(f"{x:^{max_len_left}}|{y:^{max_len_right}}")
    print(f"{dash * max_len_left}+{dash * max_len_right}")
    for i in range(von, bis + 1):
        print(f"{i:{max_len_left}}|{fkt(i):{max_len_right}}")


from tabulate import tabulate  # Ich habe es auch einfacher gemacht mit package "tabulate"


def datatabelle(fkt, von, bis):
    data = []
    for i in range(von, bis + 1):
        data.append([i, fkt(i)])
    col_names = ["x", "y"]
    print(tabulate(data, headers=col_names))


if __name__ == "__main__":
    # wertetabelle(quadrat, 2, 20)
    # wertetabelle(mult, 1, 5)
    datatabelle(quadrat, 90002, 90020)
    datatabelle(mult, 1, 5)
