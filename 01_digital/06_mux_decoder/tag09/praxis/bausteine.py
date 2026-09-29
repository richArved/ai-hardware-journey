"""Tag 9: einfache Python-Modelle und ihre Prüfung.

Beginne mit mux2, danach mux4. Alle Eingangsbits müssen 0 oder 1 sein.
Die Tests unten prüfen Python-Funktionen, NICHT deine Digital-Schaltungen.
Keine Imports oder zusätzlichen Pakete nötig.
"""


def mux2(s, d0, d1):
    # s wählt den Eingang. Zurückgegeben wird dessen Datenwert.
    if s == 0:
        return d0
    return d1


def mux4(s1, s0, d0, d1, d2, d3):
    # Zwei Auswahlbits ergeben einen Index von 0 bis 3.
    index = 2 * s1 + s0
    if index == 0:
        return d0
    if index == 1:
        return d1
    if index == 2:
        return d2
    return d3


def decoder3(a2, a1, a0):
    index = 4 * a2 + 2 * a1 + a0
    # Die Liste ist geordnet als Y0, Y1, ..., Y7.
    ausgaenge = [0, 0, 0, 0, 0, 0, 0, 0]
    ausgaenge[index] = 1
    return ausgaenge


def priority8(eingaenge):
    # Liste: I0, I1, ..., I7. Später gefundene Einsen haben Vorrang.
    gewinner = 0
    none = 1
    for index in range(8):
        if eingaenge[index] == 1:
            gewinner = index
            none = 0
    # gewinner ist eine Zahl von 0 bis 7, none ein zusätzliches Bit.
    return gewinner, none


def majority3(a, b, c):
    anzahl_einsen = a + b + c
    if anzahl_einsen >= 2:
        return 1
    return 0


def majority3_mux8(a, b, c):
    # Der MUX liest die fest verdrahteten Ausgangswerte der Wahrheitstabelle.
    daten = [0, 0, 0, 1, 0, 1, 1, 1]
    index = 4 * a + 2 * b + c
    return daten[index]


def pruefe_modelle():
    # assert prüft eine Aussage. Ist sie falsch, stoppt Python mit einem Fehler.
    # Die Sollwerte entstehen hier auf anderem Weg als in der Modellfunktion.
    anzahl = 0
    for s in range(2):
        for d0 in range(2):
            for d1 in range(2):
                soll = int((not s and d0) or (s and d1))
                assert mux2(s, d0, d1) == soll, (s, d0, d1)
                anzahl = anzahl + 1
    print("2:1-MUX:", anzahl, "Python-Fälle korrekt")

    anzahl = 0
    for auswahl in range(4):
        s1 = auswahl // 2
        s0 = auswahl % 2
        for nummer in range(16):
            # Genau vier Zeichen: z. B. '0101'. Jedes Zeichen wird zu int.
            bits = bin(nummer)[2:].zfill(4)
            d0 = int(bits[0])
            d1 = int(bits[1])
            d2 = int(bits[2])
            d3 = int(bits[3])
            # Derselbe Aufbau wie beim MUX-Baum aus drei 2:1-MUX.
            links = mux2(s0, d0, d1)
            rechts = mux2(s0, d2, d3)
            soll = mux2(s1, links, rechts)
            assert mux4(s1, s0, d0, d1, d2, d3) == soll, (auswahl, nummer)
            anzahl = anzahl + 1
    print("4:1-MUX:", anzahl, "Python-Fälle korrekt")

    for nummer in range(8):
        bits = bin(nummer)[2:].zfill(3)
        a2 = int(bits[0])
        a1 = int(bits[1])
        a0 = int(bits[2])
        ergebnis = decoder3(a2, a1, a0)
        # Unabhängige Prüfung über die acht Minterme.
        for index in range(8):
            adresse = bin(index)[2:].zfill(3)
            soll = int(a2 == int(adresse[0]) and
                       a1 == int(adresse[1]) and a0 == int(adresse[2]))
            assert ergebnis[index] == soll, (nummer, index)
        assert sum(ergebnis) == 1
    print("3:8-Decoder: 8 Python-Fälle korrekt")

    for nummer in range(256):
        bits = bin(nummer)[2:].zfill(8)  # Links steht I7, rechts I0.
        eingaenge = []
        for index in range(8):
            eingaenge.append(int(bits[7 - index]))
        gewinner, none = priority8(eingaenge)
        # Kontrollweg: von der höchsten Priorität nach unten suchen.
        soll_gewinner = 0
        soll_none = 1
        for index in range(7, -1, -1):
            if eingaenge[index] == 1:
                soll_gewinner = index
                soll_none = 0
                break  # Die erste gefundene Eins ist bereits die höchste.
        assert gewinner == soll_gewinner and none == soll_none, nummer
    print("8:3-Prioritätsencoder: 256 Python-Fälle korrekt")

    for a in range(2):
        for b in range(2):
            for c in range(2):
                soll = int((a and b) or (a and c) or (b and c))
                assert majority3(a, b, c) == soll, (a, b, c)
                assert majority3_mux8(a, b, c) == soll, (a, b, c)
    print("Majority3 und 8:1-MUX: jeweils 8 Python-Fälle korrekt")
    print("Damit sind die Python-Modelle geprüft, noch keine Simulator-Schaltungen.")


if __name__ == "__main__":
    # Ändere zum Lernen zuerst nur diese Eingaben und sage das Ergebnis voraus.
    print("Beispiel mux2(0, 1, 0):", mux2(0, 1, 0))
    pruefe_modelle()
