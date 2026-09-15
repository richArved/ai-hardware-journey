def to_bin(value: int, bits: int) -> str:
    if bits < 1:
        raise ValueError("Die Bitbreite muss mindestens 1 sein.")

    # ** bedeutet Potenz. or heißt: Mindestens eine Bedingung trifft zu.
    if value < 0 or value > 2**bits - 1:
        raise ValueError("Die Zahl passt nicht in die Bitbreite.")

    mit_prafix = bin(value) 
    wo_präfix = mit_prafix[2:]  # Entfernt das '0b' Präfix 
    zu_füllen = bits - len(wo_präfix)  # Berechnet, wie viele Nullen hinzugefügt werden müssen
    return '0' * zu_füllen + wo_präfix  # Fügt die führenden Nullen hinzu und gibt die Binärzahl zurück

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

def from_twos_complement(value: int, bits: int) -> int:
    if bits < 1:
        raise ValueError("Die Bitbreite muss mindestens 1 sein.")

    if value < 0 or value > 2**bits - 1:
        raise ValueError("Die Zahl passt nicht in die Bitbreite.")

    grenze = 2**(bits - 1)

    if value < grenze:
         return value

    return value - 2**bits

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