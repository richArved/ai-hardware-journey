"""Referenz für kleine K-Map-Aufgaben: exakte minimale SOP.

Erst von Hand lösen, dann vergleichen. Nur Python-Standardbibliothek.
Kosten: zuerst Anzahl Produktterme, dann Anzahl Literale.
"""
import argparse
import itertools
import json
from pathlib import Path


def combine(left, right):
   # Überprüft ob die beiden Bitmuster gleich lang sind. Wenn nicht, wird die Funktion mit None abgebrochen
    if len(left) != len(right):
        return None
    # Liste, in der das kombinierte Muster Zeichen für Zeichen zusammengesetzt wird.
    result = []
    # Dieser Zähler hält fest, an wie vielen Stellen sich die beiden Muster unterscheiden
    differences = 0
    # zip nimmt Zeichen für Zeichen parallel aus beiden Strings, wie ein Reißverschluss
    for a, b in zip(left, right):
        # Fall 1: die beiden Zeichen sind gleich oder haben bereits ein "-", dann wird der Wert unverändert in result übernommen.
        if a == b:
            result.append(a)
        # Fall 2:
        elif a == "-" or b == "-":
            return None
        else:
            differences += 1
            result.append("-")
    if differences == 1:
        return "".join(result)
    return None


def covers(pattern, index):
    bits = format(index, f"0{len(pattern)}b")
    return len(bits) == len(pattern) and all(a == "-" or a == b for a, b in zip(pattern, bits))


def prime_implicants(n, ones, dont_cares):
    current = {format(i, f"0{n}b") for i in ones | dont_cares}
    primes = set()
    while current:
        used = set()
        following = set()
        for left, right in itertools.combinations(sorted(current), 2):
            merged = combine(left, right)
            if merged is not None:
                used.update((left, right))
                following.add(merged)
        primes.update(current - used)
        current = following
    return sorted(p for p in primes if any(covers(p, i) for i in ones))


def minimize(n, ones, dont_cares=()):
    if type(n) is not int or not 1 <= n <= 4:
        raise ValueError("Dieses Lernprogramm unterstützt 1 bis 4 Eingänge.")
    ones, dont_cares = set(ones), set(dont_cares)
    if any(type(i) is not int or not 0 <= i < 2**n for i in ones | dont_cares):
        raise ValueError("Indizes müssen ganze Zahlen innerhalb der Bitbreite sein.")
    if ones & dont_cares:
        raise ValueError("Einerindizes und Don't-Cares müssen getrennt sein.")
    if not ones:
        return []
    primes = prime_implicants(n, ones, dont_cares)
    # Kleine Aufgaben: alle Abdeckungen nach steigender Termzahl durchsuchen.
    for count in range(1, len(primes) + 1):
        candidates = []
        for selection in itertools.combinations(primes, count):
            if all(any(covers(p, i) for p in selection) for i in ones):
                literals = sum(len(p) - p.count("-") for p in selection)
                candidates.append((literals, selection))
        if candidates:
            return list(min(candidates)[1])
    raise RuntimeError("Keine Abdeckung gefunden.")


def expression(patterns):
    if not patterns:
        return "0"
    terms = []
    for pattern in patterns:
        literals = []
        for name, bit in zip("ABCD", pattern):
            if bit == "0":
                literals.append("!" + name)
            elif bit == "1":
                literals.append(name)
        if not literals:
            return "1"
        terms.append(" * ".join(literals))
    return " + ".join(terms)


def verify(n, ones, dont_cares, patterns):
    """Prüfe alle festgelegten Zeilen; X-Zeilen sind frei."""
    for index in range(2**n):
        if index in dont_cares:
            continue
        actual = any(covers(p, index) for p in patterns)
        if actual != (index in ones):
            return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fall", type=int, choices=range(1, 11))
    group.add_argument("--alle", action="store_true")
    args = parser.parse_args()
    cases = json.loads(Path(__file__).with_name("faelle.json").read_text())
    for case in cases:
        if args.fall is not None and case["fall"] != args.fall:
            continue
        n, ones, dc = case["n"], set(case["ones"]), set(case["dont_cares"])
        patterns = minimize(n, ones, dc)
        assert verify(n, ones, dc, patterns)
        print(f"Fall {case['fall']}: {expression(patterns)}")
        print("  Muster:", patterns)
        print("  Terme:", len(patterns), "Literale:", sum(len(p)-p.count('-') for p in patterns))
        print("  Alle festgelegten Tabellenzeilen geprüft.")
