"""Tag 8: derselbe Minimierer, mit einfachen Python-Bausteinen.

Beginne nur mit combine. Die weiteren Funktionen kannst du später lesen.
Keine Imports, Mengen, List Comprehensions, Rekursion oder verschachtelten
Kurzschreibweisen. Mehr Zeilen bedeuten hier kleinere einzelne Schritte.

0 und 1 im Muster sind EINGANGSBITS. Ein '-' erlaubt beide Werte.
Die Einerindizes sagen dagegen, wo der AUSGANG Y gleich 1 sein soll.
"""


def combine(muster_links, muster_rechts):
    """Zwei passende Gruppen verbinden. Sonst None zurückgeben."""
    if len(muster_links) != len(muster_rechts):
        return None

    ergebnis = ""  # Ein zunächst leerer Text, keine Liste.
    unterschiede = 0

    # position läuft beispielsweise durch 0, 1 und 2.
    for position in range(len(muster_links)):
        zeichen_links = muster_links[position]
        zeichen_rechts = muster_rechts[position]

        if zeichen_links == zeichen_rechts:
            # Gleiche Zeichen behalten. Auch '-' gegen '-' ist gleich!
            ergebnis = ergebnis + zeichen_links
        else:
            # Hier sind die Zeichen bereits UNTERSCHIEDLICH.
            # Ein vorhandener Strich muss beim Partner an derselben Stelle sein.
            if zeichen_links == "-":
                return None
            if zeichen_rechts == "-":
                return None

            # Jetzt bleibt nur noch 0 gegen 1 oder 1 gegen 0 übrig.
            unterschiede = unterschiede + 1
            ergebnis = ergebnis + "-"

    # Wieder außerhalb der Schleife: alle Positionen wurden verglichen.
    if unterschiede == 1:
        return ergebnis
    return None


def covers(muster, index):
    """Liegt diese Zelladresse in der Gruppe? Beispiel: '10-' enthält 5."""
    bits = bin(index)[2:]
    bits = bits.zfill(len(muster))
    if len(bits) != len(muster):
        return False

    for position in range(len(muster)):
        if muster[position] != "-":
            if muster[position] != bits[position]:
                return False
    return True


def prime_implicants(anzahl_eingaenge, einerindizes, dont_cares):
    """Gruppen vergrößern, bis sie nicht mehr vergrößert werden können."""
    aktuelle_gruppen = []
    primimplikanten = []

    for index in list(einerindizes) + list(dont_cares):
        muster = bin(index)[2:]
        muster = muster.zfill(anzahl_eingaenge)
        if muster not in aktuelle_gruppen:
            aktuelle_gruppen.append(muster)

    while len(aktuelle_gruppen) > 0:
        benutzte_gruppen = []
        neue_gruppen = []

        # Alle Paare vergleichen. j beginnt hinter i, damit jedes Paar
        # nur einmal vorkommt und keine Gruppe mit sich selbst verglichen wird.
        for i in range(len(aktuelle_gruppen)):
            for j in range(i + 1, len(aktuelle_gruppen)):
                links = aktuelle_gruppen[i]
                rechts = aktuelle_gruppen[j]
                kombiniert = combine(links, rechts)

                if kombiniert is not None:
                    if links not in benutzte_gruppen:
                        benutzte_gruppen.append(links)
                    if rechts not in benutzte_gruppen:
                        benutzte_gruppen.append(rechts)
                    if kombiniert not in neue_gruppen:
                        neue_gruppen.append(kombiniert)

        for gruppe in aktuelle_gruppen:
            if gruppe not in benutzte_gruppen:
                if gruppe not in primimplikanten:
                    primimplikanten.append(gruppe)

        aktuelle_gruppen = neue_gruppen

    # Gruppen, die nur Don't-Cares enthalten, brauchen wir nicht.
    brauchbare_gruppen = []
    for gruppe in primimplikanten:
        enthaelt_eine_eins = False
        for index in einerindizes:
            if covers(gruppe, index):
                enthaelt_eine_eins = True
        if enthaelt_eine_eins:
            brauchbare_gruppen.append(gruppe)

    return sorted(brauchbare_gruppen)


def minimize(anzahl_eingaenge, einerindizes, dont_cares=()):
    """Wähle möglichst wenige Terme, bei Gleichstand möglichst wenige Literale."""
    if type(anzahl_eingaenge) is not int:
        raise ValueError("Die Eingangsanzahl muss eine ganze Zahl sein.")
    if anzahl_eingaenge < 1 or anzahl_eingaenge > 4:
        raise ValueError("Erlaubt sind 1 bis 4 Eingänge.")

    einerindizes = list(einerindizes)
    dont_cares = list(dont_cares)
    for index in einerindizes + dont_cares:
        if type(index) is not int:
            raise ValueError("Ein Index muss eine ganze Zahl sein.")
        if index < 0 or index >= 2**anzahl_eingaenge:
            raise ValueError("Ein Index liegt außerhalb der Bitbreite.")
    for index in einerindizes:
        if index in dont_cares:
            raise ValueError("Eine Zelle darf nicht gleichzeitig 1 und Don't-Care sein.")

    if len(einerindizes) == 0:
        return []  # Keine Einsen: Y = 0.

    gruppen = prime_implicants(anzahl_eingaenge, einerindizes, dont_cares)
    beste_auswahl = None
    beste_termzahl = len(gruppen) + 1
    beste_literalzahl = anzahl_eingaenge * len(gruppen) + 1

    # Jede Gruppe kann ausgewählt sein (1) oder nicht (0).
    # Bei drei Gruppen: 001 nimmt nur die letzte, 101 die erste und letzte.
    # So probieren wir alle Auswahlen durch, ohne zusätzliche Bibliothek.
    for nummer in range(1, 2**len(gruppen)):
        auswahlbits = bin(nummer)[2:]
        auswahlbits = auswahlbits.zfill(len(gruppen))
        auswahl = []
        for position in range(len(gruppen)):
            if auswahlbits[position] == "1":
                auswahl.append(gruppen[position])

        alle_einsen_abgedeckt = True
        for index in einerindizes:
            gefunden = False
            for gruppe in auswahl:
                if covers(gruppe, index):
                    gefunden = True
            if gefunden == False:
                alle_einsen_abgedeckt = False

        if alle_einsen_abgedeckt:
            termzahl = len(auswahl)
            literalzahl = 0
            for gruppe in auswahl:
                for zeichen in gruppe:
                    if zeichen != "-":
                        literalzahl = literalzahl + 1

            besser = False
            if termzahl < beste_termzahl:
                besser = True
            elif termzahl == beste_termzahl:
                if literalzahl < beste_literalzahl:
                    besser = True
                elif literalzahl == beste_literalzahl:
                    # Bei gleichen Kosten dieselbe feste Reihenfolge wie
                    # die Referenz wählen (alphabetischer Listenvergleich).
                    if auswahl < beste_auswahl:
                        besser = True

            if besser:
                beste_auswahl = auswahl
                beste_termzahl = termzahl
                beste_literalzahl = literalzahl

    return beste_auswahl


def expression(musterliste):
    """Beispiel: ['10-'] wird zum lesbaren Text 'A * !B'."""
    if len(musterliste) == 0:
        return "0"

    namen = "ABCD"
    gleichung = ""
    for muster in musterliste:
        term = ""
        for position in range(len(muster)):
            literal = ""
            if muster[position] == "0":
                literal = "!" + namen[position]
            if muster[position] == "1":
                literal = namen[position]

            if literal != "":
                if term != "":
                    term = term + " * "
                term = term + literal

        if term == "":
            return "1"  # Nur Striche: alle Eingangskombinationen erlaubt.
        if gleichung != "":
            gleichung = gleichung + " + "
        gleichung = gleichung + term

    return gleichung


def verify(anzahl_eingaenge, einerindizes, dont_cares, musterliste):
    """Stimmt die vereinfachte Gleichung an jeder festgelegten Tabellenzeile?"""
    for index in range(2**anzahl_eingaenge):
        if index not in dont_cares:
            erwartet = False
            if index in einerindizes:
                erwartet = True

            berechnet = False
            for muster in musterliste:
                if covers(muster, index):
                    berechnet = True

            if erwartet != berechnet:
                return False
    return True


# Dieser Abschnitt läuft nur beim direkten Start dieser Datei.
# Beim Importieren stehen nur die Funktionen bereit.
if __name__ == "__main__":
    print("Unser Beispiel: 100 und 101")
    print("Gemeinsames Muster:", combine("100", "101"))

    # Hier kannst du deine Aufgabe eintragen. Keine Installation notwendig.
    anzahl_eingaenge = 3
    einerindizes = [4, 5]
    dont_cares = []

    loesung = minimize(anzahl_eingaenge, einerindizes, dont_cares)
    print("Gruppen:", loesung)
    print("Y =", expression(loesung))
    print("Alle festgelegten Zeilen korrekt:",
          verify(anzahl_eingaenge, einerindizes, dont_cares, loesung))
