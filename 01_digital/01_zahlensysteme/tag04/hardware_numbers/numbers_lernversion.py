
def binaer_schritte():
    
    value = 6
    bits = 4

    # value ist eine Zahl (int), mit der Python rechnen kann.
    print("1. Zahl:", value)
    print("   Typ:", type(value))

    # bin ist eine eingebaute Funktion. Sie liefert TEXT (str).
    # 0b ist ein Präfix: Es sagt uns, dass die Ziffern binär gemeint sind.
    mit_praefix = bin(value)
    print("2. bin(value):", mit_praefix)
    print("   Typ:", type(mit_praefix))

    # Zeichenpositionen beginnen bei 0:
    # Text:       0 b 1 1 0
    # Position:   0 1 2 3 4
    # [2:] heißt: ab Position 2 bis zum Ende übernehmen.
    ohne_praefix = mit_praefix[2:]
    print("3. Nach [2:]:", ohne_praefix)

    # zfill ist eine Methode von Texten: Aufruf mit Punkt hinter dem Text.
    # Sie ergänzt links Nullen BIS zur gewünschten Gesamtlänge.
    # Sie fügt nicht pauschal bits Nullen hinzu und kürzt zu lange Texte nicht.
    aufgefuellt = ohne_praefix.zfill(bits)
    print("4. Nach zfill(bits):", aufgefuellt)


def to_bin(value: int, bits: int) -> str:
    # Die Einrückung ordnet diese Anweisungen der Funktion zu.
    if bits < 1:
        raise ValueError("Die Bitbreite muss mindestens 1 sein.")

    # ** bedeutet Potenz. or heißt: Mindestens eine Bedingung trifft zu.
    if value < 0 or value > 2**bits - 1:
        raise ValueError("Die Zahl passt nicht in die Bitbreite.")

    # Bewusst einzelne Schritte statt einer schwer lesbaren Kurzform.
    mit_praefix = bin(value)
    ohne_praefix = mit_praefix[2:]
    ergebnis = ohne_praefix.zfill(bits)

    return ergebnis

def to_hex(value: int, bits: int) -> str:
    if bits < 1:
        raise ValueError("Die Bitbreite muss mindestens 1 sein.")

    if value < 0 or value > 2**bits - 1:
        raise ValueError("Die Zahl passt nicht in die Bitbreite.")
    abschnitt = hex(value)
    rm_abschnitt = abschnitt[2:]
    up_abschnitt = rm_abschnitt.upper()
    hex_len = (bits + 3) // 4
    solution = up_abschnitt.zfill(hex_len)
    return solution

def from_twos_complement(raw: int, bits: int) -> int:
    if bits < 1:
        raise ValueError("Die Bitbreite muss mindestens 1 sein.")

    if raw < 0 or raw > 2**bits - 1:
        raise ValueError("Das Bitmuster passt nicht in die Bitbreite.")
    
    grenze = 2**(bits - 1)

    if raw < grenze:
        return raw

    return raw - 2**bits

ergebniss_c = from_twos_complement(127, 8)
print("5. Rückgabewert von from_twos_complement(127, 8):", ergebniss_c)
ergebniss_d = from_twos_complement(128, 8)
print("6. Rückgabewert von from_twos_complement(128, 8):", ergebniss_d)
ergebniss_e = from_twos_complement(255, 8)
print("7. Rückgabewert von from_twos_complement(255, 8):", ergebniss_e)     

def add_with_overflow_flag(a: int, b: int, bits: int) -> tuple[int, bool]:
    # 1. Die Bitbreite muss gültig sein.
    if bits < 1:
        raise ValueError("Die Bitbreite muss mindestens 1 sein.")

    # 2. Erlaubten Zahlenbereich im Zweierkomplement bestimmen.
    minimum = -(2**(bits - 1))
    maximum = 2**(bits - 1) - 1

    # 3. Beide Eingabezahlen müssen in diesen Bereich passen.
    if a < minimum or a > maximum:
        raise ValueError("a passt nicht in die Bitbreite.")

    if b < minimum or b > maximum:
        raise ValueError("b passt nicht in die Bitbreite.")

    # 4. Mathematisch richtige Summe berechnen.
    summe = a + b

    # 5. Prüfen, ob die Summe außerhalb des erlaubten Bereichs liegt.
    overflow = summe < minimum or summe > maximum

    # 6. Nur die angegebene Anzahl Bits behalten.
    raw = summe % (2**bits)

    # 7. Das gespeicherte Bitmuster als signed Zahl interpretieren.
    ergebnis = from_twos_complement(raw, bits)

    # 8. Gespeicherte Zahl und Overflow gemeinsam zurückgeben.
    return ergebnis, overflow

# Dieser Block läuft nur, wenn du die Datei als Programm startest.
# Beim Importieren ihrer Funktionen läuft er nicht.
if __name__ == "__main__":
    binaer_schritte()
    print("5. Rückgabewert von to_bin(6, 4):", to_bin(6, 4))

    # Deine ersten Experimente: Ändere oben in binaer_schritte
    # bits von 4 auf 8 und starte erneut. Ändere danach value von 6 auf 9.
    # Die anderen drei Funktionen rufen wir erst auf, wenn wir sie bearbeiten.
