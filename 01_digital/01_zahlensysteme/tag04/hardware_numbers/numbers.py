"""Tag 4: Implementiere die vier Funktionen gemäß README.md.

Nur Python-Integer verwenden, keine Beschränkung auf 8/16/32/64 Bit.
"""


def to_bin(value: int, bits: int) -> str:
    if bits < 1:
        raise ValueError("bits must be at least 1")
    if not (0 <= value < 2 ** bits):
        raise ValueError("value does not fit in the specified number of bits")
    return bin(value)[2:].zfill(bits)


def to_hex(value: int, bits: int) -> str:
    """Unsigned value als ceil(bits/4) große Hexziffern ohne Präfix.

    Führende Nullen beibehalten. ValueError bei bits < 1 oder wenn value
    nicht in die angegebene Bitbreite passt (auch bei bits % 4 != 0).
    """
    raise NotImplementedError("TODO: Hexdarstellung")


def from_twos_complement(raw: int, bits: int) -> int:
    """Unsigned Bitmuster raw als vorzeichenbehaftete Zahl interpretieren.

    ValueError bei bits < 1 oder raw außerhalb 0 .. 2**bits - 1.
    """
    raise NotImplementedError("TODO: Zweierkomplement dekodieren")


def add_with_overflow_flag(a: int, b: int, bits: int) -> tuple[int, bool]:
    """Zwei signed Zahlen addieren: (signed Ergebnis mit Wraparound, Overflow).

    Operanden müssen in -2**(bits-1) .. 2**(bits-1)-1 liegen.
    ValueError bei bits < 1 oder ungültigen Operanden.
    Overflow meint signed Overflow, nicht unsigned Carry.
    """
    raise NotImplementedError("TODO: Addition mit Overflow")
