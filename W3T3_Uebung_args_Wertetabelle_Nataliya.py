import matplotlib.pyplot as plt
import numpy as np

from tabulate import tabulate  # Ich habe es auch einfacher gemacht mit package "tabulate"


# TableFormat = namedtuple("TableFormat", ["lineabove", "linebelowheader",
#                                          "linebetweenrows", "linebelow",
#                                          "headerrow", "datarow",
#                                          "padding", "with_header_hide"])


def quadrat(x):
    return x ** 2


def mult(x):
    return x * 100 - 5000


def wertetabelle(fkt, von, bis):
    max_len_left = 0
    max_len_right = 0
    for i in range(von, bis + 1):
        if len(str(i)) >= max_len_left:
            max_len_left = len(str(i)) + 1
        if len(str(fkt(i))) >= max_len_right:
            max_len_right = len(str(fkt(i))) + 1
        # print(len(str(fkt(i))))
    xstr, ystr, dash = "x", "y", "-"
    print(f"{xstr:^{max_len_left}}|{ystr:^{max_len_right}}")
    print(f"{dash * max_len_left}+{dash * max_len_right}")
    for i in range(von, bis + 1):
        print(f"{i:{max_len_left}}|{fkt(i):{max_len_right}}")

    x = np.linspace(von, bis, (bis - von) * 100)
    # the function, which is y = x^2 here
    y = fkt(x)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x, y, 'r')

    # show the plot
    plt.show()


def datatabelle(fkt, von, bis):
    data = []
    for i in range(von, bis + 1):
        data.append([i, fkt(i)])
    col_names = ["x", "y"]
    print(tabulate(data, headers=col_names, tablefmt="orgtbl"))
    # floatfmt="g", numalign="decimal", stralign="left",
    # missingval="")


if __name__ == "__main__":
    wertetabelle(quadrat, 2, 20)
    wertetabelle(mult, 100, 500)
    datatabelle(quadrat, 90002, 90020)
    datatabelle(mult, 1, 5)
