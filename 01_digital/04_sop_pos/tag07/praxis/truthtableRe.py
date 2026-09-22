def minterm(names: list[str], bits: str) -> str:

    # Leere Liste für die Literals
    literals = []
    # Die Tabelle soll im Reißverschluss-prinzip gelesen werden
    for name, bit in zip(names, bits):
        # Wenn bit = 0 ist an den name vorne eine ! ranhängen
        if bit == "0":
            literal = "!" + name
            #Wenn bit = 1 name unverändert lassen
        else:
            literal = name
        # Jeweils ein Literal an die Liste literals hinten ranhängen
        literals.append(literal)
    # Die ganze Liste verbinden
    term = " * ".join(literals)
    return term

def maxterm(names: list[str], bits: str) -> str:

    literals = []

    for name, bit in zip(names, bits):
        if bit == "1":
            literal = "!" + name
        else:
            literal = name
        literals.append(literal)
    term = " + ".join(literals)
    return "(" + term + ")"

def row_bits(index: int, n: int) -> str:
    # Zeigt die Zahl als 0b Binär an
    binaer = bin(index)
    #Nimmt nur die Zeichen ab der 2 Position
    binaer_kurz = binaer[2:]
    # füllt die Zahl auf 3 Stellen mit 0 auf
    bits = binaer_kurz.zfill(n)
    return bits

def validate_table(names: list[str], outputs: list[int]) -> None:
    if not names:
        raise ValueError("names must not be empty")
    if len(outputs) != 2 ** len(names):
        raise ValueError("outputs must contain one value for each input combination")
    if any(output not in (0, 1) for output in outputs):
        raise ValueError("outputs must contain only 0 or 1")

def canonical_sop(names: list[str], outputs: list[int]) -> str:


    validate_table(names, outputs)

    if outputs.count(1) == 0:
        return "0"
    if outputs.count(0) == 0:
        return "1"

    n =len(names)
    terms = []

    for index, output in enumerate(outputs):
        if output == 1:
            bits = row_bits(index, n)
            term = minterm(names, bits)
            terms.append(term)
    return " + ".join(terms)



def canonical_pos(names: list[str], outputs: list[int]) -> str:

    validate_table(names, outputs)

    if outputs.count(1) == 0:
        return("0")
    if outputs.count(0) == 0:
        return "1"

    n = len(names)
    terms = []

    for index, output in enumerate(outputs):
        if output == 0:
            bits = row_bits(index, n)
            term = maxterm(names, bits)
            terms.append(term)

    return (" * ").join(terms)


if __name__ == "__main__":
    bsp_names = ["A", "B"]
    bsp_outputs = [0, 0, 1, 1]

    print("Aufgabe 7")
    print("SOP:", canonical_sop(bsp_names, bsp_outputs))
    print("POS:", canonical_pos(bsp_names, bsp_outputs))


if __name__ == "__main__":
    print("8a")
    names_3 = ["A", "B", "C"]

    # Majority3: 1, wenn mindestens zwei Eingänge 1 sind
    maj = [0, 0, 0, 1, 0, 1, 1, 1]
    print("Majority3 SOP:", canonical_sop(names_3, maj))
    print("Majority3 POS:", canonical_pos(names_3, maj))
    print()

    # XOR3: 1, wenn ungerade viele Einsen
    xor = [0, 1, 1, 0, 1, 0, 0, 1]
    print("XOR3 SOP:", canonical_sop(names_3, xor))
    print("XOR3 POS:", canonical_pos(names_3, xor))
    print()

    print(" 8b ")
    names_2 = ["A", "B"]
    print("Alles 0 (Erwartung '0'):", canonical_sop(names_2, [0, 0, 0, 0]))
    print("Alles 1 (Erwartung '1'):", canonical_sop(names_2, [1, 1, 1, 1]))
    print("1 Variable (Erwartung 'A'):", canonical_sop(["A"], [0, 1]))
    print()

    print("8d")

    # Zu wenige Ausgangswerte
    try:
        canonical_sop(["A", "B"], [0, 1, 0])
        print("Fehler: Zu wenige Werte wurden fälschlicherweise akzeptiert!")
    except ValueError:
        print("Erfolg: 3 Werte bei 2 Variablen warf ValueError.")

    # Ungültiger Wert (2)
    try:
        canonical_sop(["A", "B"], [0, 1, 2, 0])
        print("Fehler: Zahl 2 wurde fälschlicherweise akzeptiert!")
    except ValueError:
        print("Erfolg: Wert 2 warf ValueError.")

    # Keine Variablen übergeben
    try:
        canonical_sop([], [0])
        print("Fehler: Leere Variablenliste wurde akzeptiert!")
    except ValueError:
        print("Erfolg: Keine Variablen warf ValueError.")
