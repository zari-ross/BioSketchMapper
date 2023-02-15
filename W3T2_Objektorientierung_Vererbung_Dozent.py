# ===================================================================
from W3T1_Uebung_Becher_Dozent import Becher


class Person():
    """
    Das Attribut 'name' soll von außen nicht geändert werden können. Die einzige
    Möglichkeit des Auslesens und der Änderung des Namens soll eine Methode sein.
    Denn dann kann einem Attribut kein beliebiger Phantasieinhalt gegeben werden,
    sondern es kann eine Plausibilitätsprüfung stattfinden. Bei Vornamen z.B.
    ein Zugriff auf ein Register gültiger Namen.
    Die Kennzeichnung als privates Attribut erfolgt durch zwei führende und ohne
    abschließende Unterstriche.
    Das sorgt für ein Namemangling ('Namensverstümmelung').

    Elemente (Attribute und Methoden) mit führenden und abschließenden Unterstrichen
    sind von der Namensverstümmelung nicht betroffen und für besondere Zwecke vorgesehen.
    In der Regel sind dies Benennungen, die nicht von Programmierenden vorgenommen werden
    und somit kann die Wahrscheinlichkeit eines Namenskonfliktes gering gehalten werden kann.
    Außerdem sind diese Variablen und Methoden üblicherweise Namen vom System.

    Eine Klasse gilt als vollständig gekapselt, wenn kein einziges Attribut von
    außerhalb zugreifbar ist. Alle Attribute sind nur noch durch Methoden erreichbar:
    a) get-Methode (get_var() oder getVar()) liefert den Wert der Variablen var zurück
    b) set-Methode (set_var(var) oder setVar(var)) gibt der Variablen self.var den Wert var.
       Hier können und sollten Plausibilitätstests durchgeführt werden.
    """
    __name: str = None
    __dreizehn__: int = 13

    def __init__(self, name):
        self.__name = name

    def repraesentation(self):
        # __name__ ist eine Information vom System über die aktuelle Datei
        return '<' + __name__ + '.' + type(self).__name__ + ' object at ' + f'0x{id(self):016X}' + '>'


# ===================================================================

class Sichtbarkeit():
    """
    Ein Attribut ohne Unterstriche ist immer public und von überall sicht- und änderbar
    """
    public_attribut = "public Attribut"

    """
    Ein Attribut mit einem führenden und ohne abschließenden Unterstrich ist immer 
    "protected" (geschützt). Das bedeutet, es wird von der Entwicklungsumgebung 
    nicht angeboten, kann aber - bei Kenntnis des Attributs - problemlos wie "public"
    verwendet werden. Programmierende wissen allerdings offiziell nichts von der 
    Existenz solcher Elemente. Diese muss ihnen "hinter vorgehaltener Hand" mitgeteilt
    werden. 
    """
    _protected_attribut = "protected Attribut"

    """
    Ein Attribut mit zwei führenden Unterstrichen und ohne abschließende Unterstriche sind 
    "private". Sie werden von der Entwicklungsumgebung nicht angeboten und können von außerhalb
    nicht gelesen oder geändert werden.
    """
    __private_attribut = 'private Attribut'

    def public_methode(self):
        """
        Öffentlich aufrufbar.
        """
        print('public Methode')

    def _protected_methode(self):
        """
        Geschützt: nur aufrufbar, wenn davon Kenntnis besteht.
        """
        print('protected Methode')

    def __private_methode(self):
        """
        Privat: von außerhalb nicht erreichbar.
        """
        print('private Methode')

    def self_info(ich):
        """
        Entgegen vieler Meinungen ist "self" kein reserviertes Schlüsselwort.
        Es kann durch einen beliebigen anderen Variablennamen ausgetauscht werden.
        """
        print("Vom Typ:", type(ich).__name__)


# ===================================================================

class Superklasse():
    def __init__(self, test):
        print("__init__ in Superklasse")

    def methode_in_superklasse(self):
        print("methode_in_superklasse")

    def methode(self):
        print("Superklasse: methode")


# ===================================================================

class Subklasse(Superklasse):
    """
    Diese Klasse erbt von "Superklasse". Es werden alle Methoden und
    Attribute geerbt, die NICHT als privat gekennzeichnet sind!
    Verbung wird eingesetzt, um
    1) eine vorhandene Klasse um Funktionalitäten und/oder Informationen
       zu erweitern und/oder zu ändern,
    2) Code zu sparen, denn eine geerbte Methode muss nicht neu geschrieben
       bzw. kopiert werden.

    Dadurch, daß viele Funktionalitäten von "object" geerbt werden, müssen
    diese object-Methoden bereits einen Funktionskörper besitzen, d.h. sie
    sind mit irgendwas realisiert (sh. '__str__'). Dieses Können ist für selbst
    programmierte Methoden unzureichend, d.h. einige dieser Methoden müssen
    einen neuen angepassten Körper erhalten.
    Durch das Neuschreiben einer geerbten Methode bekommt die alte Methode
    neue Funktionalität. Aber erst ab der Realisierung.
    Dieses Vorgehen wird "Überschreiben" genannt.

    Jede Klasse erbt von einer anderen Klasse. Diese Vererbungskette lässt
    sich bis zu einem "Fixpunkt" zurückverfolgen: zur Klasse "object".
    "object" erbt von sich selbst und ist die Basisklasse aller Basisklassen.
    Sie verfügt über eine Grundfunktionalität, die an alle erbenden Klassen
    weitergegeben wird!
    "object" gehört zum Paket "builtins".
    """

    def __init__(self):
        super().__init__(13)
        print("__init__ in Subklasse")

    def methode_in_subklasse(self):
        print("methode_in_subklasse")

    def methode(self):
        super().methode()
        print("Subklasse: methode")


# ===================================================================

class SuperklasseA:

    def supermethode_a(self):
        print("supermethode_a")

    def supermethode_ab(self):
        print("supermethode_ab in A")


# ===================================================================

class SuperklasseB:

    def supermethode_b(self):
        print("supermethode_b")

    def supermethode_ab(self):
        print("supermethode_ab in B")


# ===================================================================

class SubklasseAB(SuperklasseA, SuperklasseB):
    """
    Kommt es bei Mehrfachvererbung zu einem Konflikt, weil es in den
    Superklassen geichnamige Methoden gibt, kann dieser gelöst werden.
    Erst einmal: wird von einer Klasse "Klasse" eine Methode aufgerufen,
    geschieht dies üblicherweise mit einem Objekt:
    obj.methode()
    Das "self" in der Methode wird automatisch die Referenz von "obj"
    annehmen, d.h. die Angabe dieses Arguments geschieht implizit.
    Beim Aufruf über den Klassennamen ("Klasse.methode()") ist kein Objekt
    involviert und self somit nicht gesetzt, was zu einem Fehler führt.
    Es funktioniert aber der explizite Aufruf:
    Klasse.methode(obj)
    Hier bekommt self die Referenz von obj explizit als Parameter zugewiesen.
    D.h. mit "SuperklasseA.methode_ab(self)" wird wirklich die methode_ab in
    SuperklasseA aufgerufen. Analog "SuperklasseB.methode_ab(self)".
    Schrittweise:
    sub ist gleichzeitig SuperklasseA-Objekt UND SuperklasseB-Objekt.
    sub.methode_ab() -> self == sub -> SuperklasseA.methode_ab() == sub.methode_ab(SuperklasseA-Objekt)
    sub.methode_ab() -> self == sub -> SuperklasseB.methode_ab() == sub.methode_ab(SuperklasseB-Objekt)
    """
    def methode(self):
        self.supermethode_a()
        self.supermethode_b()
        self.supermethode_ab()

        print()

        SuperklasseA.supermethode_a(self)
        SuperklasseB.supermethode_b(self)
        SuperklasseA.supermethode_ab(self)
        SuperklasseB.supermethode_ab(self)


# ===================================================================

def objektorientierung():
    p = Person("Bud Spencer")
    print(p)
    print(p.repraesentation())
    print(p.__dreizehn__)


# -------------------------------------------------------------------

def sichtbarkeitsdemo():
    s = Sichtbarkeit()
    print(s.public_attribut)
    print(s._protected_attribut)
    # print(s.__private_attribut)
    s.public_methode()
    s._protected_methode()
    # s.__private_methode()

    s.self_info()


# -------------------------------------------------------------------

def vererbung():
    p = Person("Bud Spencer")
    o = object()

    # sup = Superklasse()
    # sup.methode_in_superklasse()

    print()

    sub = Subklasse()
    sub.methode_in_subklasse()
    sub.methode_in_superklasse()
    sub.methode()

    sub_ab = SubklasseAB()
    sub_ab.supermethode_a()
    sub_ab.supermethode_b()
    sub_ab.supermethode_ab()

    print()

    sub_ab.methode()

# -------------------------------------------------------------------

if (__name__ == '__main__'):
    objektorientierung()
    sichtbarkeitsdemo()
    vererbung()
    b = Becher(fuellhoehe=1.0, inhalt="Kaffee", fassungsvermoegen=350)
    print(b)
