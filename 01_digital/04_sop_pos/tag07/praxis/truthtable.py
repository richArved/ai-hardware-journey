"""Tag 7: Wahrheitstabellen in kanonische SOP und POS übersetzen.

Keine Imports oder zusätzlichen Pakete nötig.
Die Ausgabetexte verwenden ! = NICHT, * = UND und + = ODER.
Das ist Logiknotation, kein ausführbarer Python-Code.
"""


def validate_table(names: list[str], outputs: list[int]) -> None:
    """Prüfe die Eingaben; bei einem Fehler wird ValueError ausgelöst.

    Wie im Aufgabenblatt setzen wir unterschiedliche, gültige Variablennamen
    und ganze Zahlen als Ausgangswerte voraus.
    """
    # len zählt die Einträge einer Liste.
    n = len(names)
    if n == 0:
        raise ValueError("Mindestens eine Eingangsvariable ist erforderlich.")

    # n Eingänge ergeben 2 hoch n mögliche Kombinationen.
    expected_rows = 2 ** n
    if len(outputs) != expected_rows:
        raise ValueError(f"Für {n} Eingänge werden {expected_rows} Ausgangswerte benötigt.")

    for output in outputs:
        if output != 0 and output != 1:
            raise ValueError("Jeder Ausgangswert muss 0 oder 1 sein.")

    # Ohne ausdrückliches return gibt eine Funktion None zurück.


def row_bits(index: int, n: int) -> str:
    """Schreibe einen gültigen Index als genau n Bits: (2, 3) -> '010'.

    Voraussetzung: n >= 1 und 0 <= index < 2**n.
    """
    binaertext = bin(index)               # Beispiel: '0b10'
    ohne_praefix = binaertext[2:]         # Beispiel: '10'
    bits = ohne_praefix.zfill(n)          # Bei n = 3: '010'
    return bits


def minterm(names: list[str], bits: str) -> str:
    """Negiere bei Bit 0 und verbinde alle Literale mit UND.

    names und bits müssen gleich lang sein; bits enthält nur '0' und '1'.
    """
    # Eingaben kommen vom Aufruf. Hier nicht durch feste Werte ersetzen!
    literals = []

    # zip verbindet Name und Bit von derselben Position.
    for name, bit in zip(names, bits):
        if bit == "0":
            literal = "!" + name
        else:
            literal = name

        # Ein Literal an die Liste anhängen; frühere Einträge bleiben erhalten.
        literals.append(literal)

    # Die ganze Liste verbinden, nicht nur das letzte einzelne literal.
    term = " * ".join(literals)
    return term


def maxterm(names: list[str], bits: str) -> str:
    """Negiere bei Bit 1 und verbinde alle Literale mit ODER.

    Voraussetzungen wie bei minterm. Die Ausgabe steht in Klammern.
    """
    literals = []

    for name, bit in zip(names, bits):
        if bit == "1":
            literal = "!" + name
        else:
            literal = name

        literals.append(literal)

    term = " + ".join(literals)
    return "(" + term + ")"


def canonical_sop(names: list[str], outputs: list[int]) -> str:
    """Verbinde die Minterme aller Einerzeilen mit ODER."""
    validate_table(names, outputs)

    # count zählt, wie oft ein bestimmter Wert in der Liste vorkommt.
    if outputs.count(1) == 0:
        return "0"
    if outputs.count(0) == 0:
        return "1"

    n = len(names)
    terms = []

    # enumerate liefert jeweils die Position (index) und den Wert (output).
    for index, output in enumerate(outputs):
        if output == 1:
            bits = row_bits(index, n)
            term = minterm(names, bits)
            terms.append(term)

    # Jeder Term beschreibt eine Einerzeile; ODER verbindet diese Fälle.
    return " + ".join(terms)


def canonical_pos(names: list[str], outputs: list[int]) -> str:
    """Verbinde die Maxterme aller Nullzeilen mit UND."""
    validate_table(names, outputs)

    if outputs.count(1) == 0:
        return "0"
    if outputs.count(0) == 0:
        return "1"

    n = len(names)
    terms = []

    for index, output in enumerate(outputs):
        if output == 0:
            bits = row_bits(index, n)
            term = maxterm(names, bits)
            terms.append(term)

    # Jeder Maxterm hat bereits Klammern. UND verbindet die Klammern.
    return " * ".join(terms)


# Dieser Block läuft beim direkten Start: python3 truthtable.py
# Beim Importieren der Funktionen in eine andere Datei läuft er nicht.
if __name__ == "__main__":
    # Die Eingaben stehen außerhalb der Funktionen und werden übergeben.
    names = ["A", "B", "C"]

    # Index:             0  1  2  3  4  5  6  7
    # Eingänge ABC:    000 001 010 011 100 101 110 111
    majority_outputs = [0, 0, 0, 1, 0, 1, 1, 1]
    xor_outputs =      [0, 1, 1, 0, 1, 0, 0, 1]

    print("Majority3")
    print("SOP:", canonical_sop(names, majority_outputs))
    print("POS:", canonical_pos(names, majority_outputs))
    print()
    print("XOR3")
    print("SOP:", canonical_sop(names, xor_outputs))
    print("POS:", canonical_pos(names, xor_outputs))
