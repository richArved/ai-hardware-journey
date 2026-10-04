"""Dein Anteil: Ersetze die zwei Platzhalter durch je eine return-Rechnung.

Annahmen: n ist eine ganze Zahl >= 1, Zeiten sind positiv und in ns.
Modell 1: n * t_fa
Modell 2: (ceil(log2(n)) + 2) * t_stufe
Modell 2 ist hierarchisches Lookahead/Prefix, kein verketteter Block-CLA.
"""
from math import ceil, log2


def delay_ripple(n, t_fa):
    return n * t_fa
    raise NotImplementedError("Ergaenze delay_ripple.")


def delay_cla(n, t_stufe):
    ebene = ceil(log2(n))
    return (ebene + 2) * t_stufe
    raise NotImplementedError("Ergaenze delay_cla.")
