# from mytools.tools

def main():
    tupel1 = tuple()
    tupel2 = ()

    print(tupel1, tupel2, type(tupel1), type(tupel2))

    # Sie sind unveränderbar.
    # Um append zu verwenden, müssen wir es in eine Liste umwandeln (konvertieren).

    tupel1 = (2, 6, 9)
    liste1 = list(tupel1)
    liste1.append(4)
    tupel2 = tuple(liste1)
    print(tupel1, tupel2, type(tupel1), type(tupel2))

    # set1 = {}
    set2 = set({2, 5, 6, 9})  # Kann initiieren sein mit einfach {}, aber auch so für dict.
    set1 = set({2, 3, 8, 9})
    print(set1, set2, type(set1), type(set2),
          set1.intersection(set2), set1.difference(set2), set1.union(set2), set1.copy())


# def add_in_remembering_environment():
#     inp = str(input("Input your words separated by commas only:"))
#     liste = list(inp.split(','))
#     print(liste)
#     try:
#         vokabeln.append(liste)
#     except:
#         vokabeln = list()
#         vokabeln.append(liste)
#     print(vokabeln)


# def hinzufuegen(vals):
#     return [v * v for v in vals]
#     liste = list(woerter.split(','))
#     vokabeln.append(liste)
#     print(vokabeln)


def hinzufuegen(woerter: list):  # , vokabeln=None
    # liste = woerter
    if len(vokabeln) != 0:
        i = 0
        check = True
        while i < len(vokabeln):
            if woerter[0] == vokabeln[i][0]:
                check = False
                for j in woerter:
                    if j not in vokabeln[i]:
                        vokabeln[i].append(j)
            i += 1
        if check:
            vokabeln.append(woerter)
    else:
        vokabeln.append(woerter)
    print(vokabeln)
    return vokabeln


def suchen(wort):
    for i in vokabeln:
        # print(i[0])
        if wort == i[0]:
            return i[1:]


def suchen_alle(wort):
    for i in vokabeln:
        # print(i[0])
        for j in i:
            if wort == j:
                # print(i.index(j))
                # if i.index(j) == 0:
                return f"{i[0]} - {', '.join(i[1:])}"


if __name__ == "__main__":
    # main()
    vokabeln = []
    hinzufuegen(['12', '1212'])
    hinzufuegen(['123', '121223'])
    hinzufuegen(['124', '12122343'])
    hinzufuegen(['124', '121223wedwedwe3'])
    hinzufuegen(['125', '12123434', '343434', '343423e2334', '3423e233434'])
    # print(vokabeln)

    print(suchen('12'))
    print(suchen('125'))

    print(suchen_alle('125'))
    print(suchen_alle('1212'))
    print(suchen_alle('343434'))
