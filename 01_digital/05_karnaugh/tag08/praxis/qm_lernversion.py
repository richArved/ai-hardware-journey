"""Eigene Umsetzung für Tag 8. Schrittweise arbeiten, Referenz erst danach lesen.

Bitmuster bestehen aus '0', '1' und '-'. Die Namen sind A, B, C, D.
Eingaben für minimize: n=1..4, ones und dont_cares als Listen gültiger Indizes.
Ungültige Bitbreiten/Indizes und überlappende Listen sollen ValueError auslösen.
"""


def combine(left, right):
    """Ein Bitunterschied bei gleichen Strichpositionen -> neues Muster, sonst None."""
    raise NotImplementedError("Schritt 1: zwei Muster vergleichen")


def covers(pattern, index):
    """True, wenn das Muster den Index abdeckt; z. B. covers('10-', 5)."""
    raise NotImplementedError("Schritt 2: ein Muster an einer Zeile prüfen")


def prime_implicants(n, ones, dont_cares):
    """Nicht weiter kombinierbare Muster ermitteln; Duplikate vermeiden."""
    raise NotImplementedError("Schritt 3: wiederholt kombinieren")


def minimize(n, ones, dont_cares=()):
    """Minimale Liste von Mustern liefern: wenigste Terme, dann Literale.

    Konstant 0: []; konstant 1: ['-' * n].
    Don't-Cares müssen nicht abgedeckt werden. Keine Einsen -> [].
    """
    raise NotImplementedError("Schritt 4: Primimplikanten auswählen")


if __name__ == "__main__":
    print("Beginne mit combine. Erwartung für '100' und '101': '10-'.")
    # Nach dem Implementieren aktivieren:
    # print(combine('100', '101'))
