"""Referenzhilfe: erst nach eigenem Versuch vergleichen. Zeiten in ns."""
from math import ceil, log2


def delay_ripple(n, t_fa):
    return n * t_fa


def delay_cla(n, t_stufe):
    # Idealisiertes hierarchisches Lookahead-/Prefix-Modell.
    return (ceil(log2(n)) + 2) * t_stufe
