class Textdateien():
    __dateiname = "C:/Users/NITru/PycharmProjects/pythonProject1/W3T4_text_output.txt"

    def text_neu_schreiben(self, text):
        # r = read
        # w = write
        # r+ = read+append
        # a = append
        datei = open(self.__dateiname, "w")
        datei.write(text)
        datei.write("\n")
        datei.close()

    def text_anhaengen(self, text, anzahl=1, sep="\n"):
        datei = open(self.__dateiname, "a")
        for i in range(0, anzahl):
            datei.write(text)
            datei.write(sep)
        datei.close()

    def text_lesen_v1(self):
        datei = open(self.__dateiname, "r")
        text = datei.read()
        datei.close()
        print(text)

    def text_lesen_v2(self):
        datei = open(self.__dateiname, "r")
        for zeile in datei:
            print("---->", zeile[:-1])
        datei.close()

    def text_lesen_anhaengen(self, text, anzahl=1, sep="\n"):
        datei = open(self.__dateiname, "r+")
        gelesen = datei.read(50)
        for i in range(0, anzahl):
            datei.write(text)
            datei.write(sep)
        datei.flush()
        datei.close()
        print("Gelesen: -->" + gelesen + "<--")


#
# if __name__ == "__main__":
#     t = Textdateien()
#     # t.text_neu_schreiben("Hallo!")
#     # t.text_anhaengen("What's up?", 4)
#     # t.text_anhaengen("Naaa", 2)
#     # t.text_anhaengen("Na", 7, " ")
#     # t.text_lesen_v1()
#     # t.text_lesen_anhaengen("Why oh why?")
#     t.text_lesen_v2()

# In Python, the flush() method is used to force the contents of a stream to be written to their underlying buffer.
# When a program writes to a stream, the data is typically buffered, which means that it is held in memory
# until enough data has accumulated to make it worth writing to disk or to some other output device.
# The flush() method ensures that any data that has been buffered is immediately written to the output device,
# so that it is available for other programs or processes to read.
#
# The flush() method is often used when writing to a file or network socket, where it is important to make sure
# that all data is written and available to be read by other programs or devices.
# For example, when writing to a log file, it is important to ensure
# that all log messages are written to the file immediately, so that they are available for analysis or debugging.
#
# In summary, flush() in Python is used to force the contents of a stream to be written
# to their underlying buffer immediately.

def myprint(nr, *args):
    text = f"({nr:02d}) "
    for arg in args:
        text += str(arg) + ", "
    print(text[:-2])


def datum():
    from datetime import datetime, date, timedelta
    jetzt = datetime.now()
    # print(f"(01) {jetzt}, typ = {type(jetzt)}")  # typ = <class 'datetime.datetime'>
    # print("(02a)", jetzt.day)
    # print("(02b)", jetzt.month)
    # print("(02c)", jetzt.year)

    kursstart = date(2023, 1, 30)
    print("(03) Kursstart:", kursstart)
    print(f"(04) {kursstart.day}.{kursstart.month}.{kursstart.year}")

    # auf den Kursstart eine Zeitspanne von 3 Wochen und 4 Tagen rechnen
    kursende = kursstart + timedelta(weeks=3, days=4)
    # print(f"(05) {kursende.day}.{kursende.month}.{kursende.year}")

    myprint(1, jetzt)
    myprint(2, jetzt.year)
    myprint(3, jetzt.month)
    myprint(4, jetzt.day)
    myprint(5, jetzt.hour)
    myprint(6, jetzt.minute)
    myprint(7, jetzt.second)
    myprint(8, jetzt.microsecond)

    myprint(9, kursstart)
    myprint(10, kursende)


if __name__ == "__main__":
    datum()
