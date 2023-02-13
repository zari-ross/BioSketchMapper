def main():
    pass


vokabeln = {}


def hinzufuegen(wort, uebersetzung):
    if not wort in vokabeln.keys():
        vokabeln[wort] = [uebersetzung]
    else:
        ueb = vokabeln[wort]
        print(ueb)
        if uebersetzung not in ueb:
            ueb.append(uebersetzung)
    print(vokabeln)


def suchenV1(wort):
    back = ""
    if wort in vokabeln.keys():
        back = wort + " - "
        eintrag = vokabeln[wort]
        for ueb in eintrag:
            back += ueb + ', '
            back = back[:-2]
    return back


def suchenV2(wort):
    back = ""
    for eintrag in vokabeln.items():
        if wort == eintrag[0] or wort in eintrag[1]:
            uebersetzung = ""  # to avoid quotes in output
            for ueb in eintrag[1]:
                uebersetzung += ueb + ', '
            back += "\n" + eintrag[0] + " - " + uebersetzung[:-2]
    return back


if __name__ == "__main__":
    # main()

    hinzufuegen('12', '1212')
    hinzufuegen('123', '121223')
    hinzufuegen('124', '12122343')
    hinzufuegen('124', '121223wedwedwe3')
    hinzufuegen('125', '121dwedwe3')

    print(suchenV1('12'))
    print(suchenV1('15'))
    print(suchenV1('124'))

    print(suchenV2('125'))
    print(suchenV2('1212'))
    print(suchenV2('343434'))
    print(suchenV2('124'))
